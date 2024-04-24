import mediapipe as mp
from helpers import *
from hand_landmarks import *

# Letter 'A'
# The letter a is defined by the two following propertes:
# - The hand(four fingers) is closed
# - the thumb is to the side of all of the fingers (not across any fingers)
# returns: true if all the above proprties are true, false otherwise
def is_letter_a(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    index_dip = index_dip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
                
    # Right Hand
    if handedness:
        return (is_facing_forward(results, landmarks) and
                is_hand_closed(landmarks) and
                thumb_tip.x > max(index_mcp.x, index_dip.x) and 
                index_tip.y > middle_pip.y and
                (normalized_slope(thumb_mcp, thumb_tip) > .7 or
                normalized_slope(thumb_mcp, thumb_tip) < -.7))
    # Left Hand
    else:
        return (is_facing_forward(results, landmarks) and
                is_hand_closed(landmarks) and
                thumb_tip.x < min(index_mcp.x, index_dip.x) and 
                index_tip.y > middle_pip.y and
                (normalized_slope(thumb_mcp, thumb_tip) > .7 or
                normalized_slope(thumb_mcp, thumb_tip) < -.7))
        
def is_letter_b(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    if handedness:
        return (is_facing_forward(results, landmarks) and 
                is_hand_open(landmarks) 
                and thumb_ip.x - thumb_tip.x > abs(thumb_tip.y - thumb_ip.y))
    else:
        return (is_facing_forward(results, landmarks) and
                is_hand_open(landmarks) 
                and thumb_tip.x - thumb_ip.x > abs(thumb_tip.y - thumb_ip.y))

                

def is_letter_c(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks) 
    pinky_mcp = pinky_mcp_lm(landmarks)
    
    return (not is_facing_forward(results, landmarks) and
            not is_facing_back_and_sideways(results, landmarks) and
            distance(index_mcp, pinky_mcp) < 0.7 * distance(index_mcp, wrist) and
            wrist.y > index_mcp.y and
            is_hand_closed_sideways(results, landmarks) and  
            not is_touching(index_tip, thumb_tip, thumb_ip) and
            not is_touching(middle_tip, thumb_tip, thumb_ip) and
            not is_touching(ring_tip, thumb_tip, thumb_ip) and
            not is_touching(pinky_tip, thumb_tip, thumb_ip))

def is_letter_d(results, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    return (is_facing_forward(results, landmarks) and
           not is_finger_open(middle_tip, middle_pip, wrist) and
           not is_finger_open(ring_tip, ring_pip, wrist) and
           not is_finger_open(pinky_tip, pinky_pip, wrist) and
           is_finger_open(index_tip, index_pip, wrist) and
           is_touching(thumb_tip, middle_tip, middle_dip))
    

def is_letter_e(results, landmarks):
    handedness = is_right_hand(results, landmarks)

    thumb_ip = thumb_ip_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_slope = normalized_slope(thumb_tip, thumb_ip)
    
    if handedness:
        return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            thumb_tip.y > index_tip.y and
            thumb_tip.y > middle_tip.y and
            thumb_tip.y > ring_tip.y and
            thumb_tip.y > pinky_tip.y and
            thumb_slope > -0.4 and
            thumb_slope < 0.4 and 
            thumb_tip.x < thumb_ip.x)
    else:
        return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            thumb_tip.y > index_tip.y and
            thumb_tip.y > middle_tip.y and
            thumb_tip.y > ring_tip.y and
            thumb_tip.y > pinky_tip.y and
            thumb_slope > -0.4 and
            thumb_slope < 0.4 and
            thumb_tip.x > thumb_ip.x)

def is_letter_f(results, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    return (is_facing_forward(results, landmarks) and
           is_finger_open(middle_tip, middle_pip, wrist) and
           is_finger_open(ring_tip, ring_pip, wrist) and
           is_finger_open(pinky_tip, pinky_pip, wrist) and
           not is_finger_open(index_tip, index_pip, wrist) and
           is_touching(index_tip, thumb_tip, thumb_ip))
 

def is_letter_g(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    return (is_hand_closed_sideways(results, landmarks) and
            wrist.y > index_mcp.y and
            is_finger_open_sideways(thumb_tip, thumb_ip, handedness) and
            is_finger_open_sideways(index_tip, index_pip, handedness) and
            not is_finger_open_sideways(middle_tip, middle_pip, handedness) and 
            not is_finger_open_sideways(ring_tip, ring_pip, handedness) and
            not is_finger_open_sideways(pinky_tip, pinky_pip, handedness)) 

def is_letter_h(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    return (is_hand_closed_sideways(results, landmarks) and
            is_finger_open_sideways(index_tip, index_pip, handedness) and
            is_finger_open_sideways(middle_tip, middle_pip, handedness) and 
            not is_finger_open_sideways(ring_tip, ring_pip, handedness) and
            not is_finger_open_sideways(pinky_tip, pinky_pip, handedness)and 
            is_touching(index_tip, middle_tip, middle_dip)) 

def is_letter_i(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    index_dip = index_dip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    if handedness: # Right hand
        return (is_facing_forward(results, landmarks) and
                thumb_tip.x > max(index_mcp.x, index_dip.x) and
                not (normalized_slope(thumb_mcp, thumb_tip) > -.8 and
                normalized_slope(thumb_mcp, thumb_tip) < 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))
    else: # Left hand
        return (is_facing_forward(results, landmarks) and
                thumb_tip.x < min(index_mcp.x, index_dip.x) and
                not (normalized_slope(thumb_mcp, thumb_tip) < .8 and
                normalized_slope(thumb_mcp, thumb_tip) > 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))


def is_letter_j(results, landmarks):
    return False

def is_letter_k(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            not is_touching(index_tip, middle_tip, middle_dip) and
            thumb_tip.x > min(index_pip.x, middle_pip.x) and
            thumb_tip.x < max(index_pip.x, middle_pip.x) and
            thumb_tip.y < index_mcp.y)
            

def is_letter_l(results, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    handedness = is_right_hand(results, landmarks)

    return (is_facing_forward(results, landmarks) and
           not is_finger_open(middle_tip, middle_pip, wrist) and
           not is_finger_open(ring_tip, ring_pip, wrist) and
           not is_finger_open(pinky_tip, pinky_pip, wrist) and
           is_finger_open(index_tip, index_pip, wrist) and
           abs(normalized_slope(index_mcp, index_tip)) - abs(normalized_slope(thumb_mcp, thumb_tip)) > 0.5)

def is_letter_m(results, landmarks):
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_dip = ring_dip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_dip = pinky_dip_lm(landmarks)
    
    return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            is_touching(thumb_tip,pinky_pip, pinky_dip) and
            is_touching(thumb_tip, ring_pip, ring_dip) and
            ring_pip.y < thumb_tip.y < pinky_pip.y)

def is_letter_n(results, landmarks):
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_dip = ring_dip_lm(landmarks)
    
    handedness = is_right_hand(results, landmarks)
    
    if handedness:
        return (is_facing_forward(results, landmarks) and
                is_hand_closed(landmarks) and
                is_touching(thumb_tip, middle_pip, middle_dip) and
                is_touching(thumb_tip, ring_pip, ring_dip) and
                middle_pip.y < thumb_tip.y < ring_pip.y and
                thumb_tip.x < middle_pip.x)
    else:
        return (is_facing_forward(results, landmarks) and
                is_hand_closed(landmarks) and
                is_touching(thumb_tip, middle_pip, middle_dip) and
                is_touching(thumb_tip, ring_pip, ring_dip) and
                middle_pip.y < thumb_tip.y < ring_pip.y and
                thumb_tip.x > middle_pip.x)
    
def is_letter_o(results, landmarks):
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    wrist = wrist_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    
    return (not is_facing_forward(results, landmarks) and
            wrist.y > index_mcp.y and
            not is_facing_back_and_sideways(results, landmarks) and
            is_hand_closed_sideways(results, landmarks) and
            (is_touching(index_tip, thumb_tip, thumb_ip) or
             is_touching(middle_tip, thumb_tip, thumb_ip) or
             is_touching(ring_tip, thumb_tip, thumb_ip) or
             is_touching(pinky_tip, thumb_tip, thumb_ip)))

def is_letter_p(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    return (not is_finger_closed_upside_down(index_tip, index_pip, wrist) and
            not is_finger_closed_upside_down(middle_tip, middle_pip, wrist) and
            is_finger_closed_upside_down(ring_tip, ring_pip, wrist) and
            is_finger_closed_upside_down(pinky_tip, pinky_pip, wrist) and
            min(index_pip.x, middle_pip.x) < thumb_tip.x < max(index_pip.x, middle_pip.x) and
            not is_touching(index_tip, middle_tip, middle_dip))
    

def is_letter_q(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    index_dip = index_dip_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    return (not is_finger_closed_upside_down(index_tip, index_pip, wrist) and
            is_finger_closed_upside_down(middle_tip, middle_pip, wrist) and
            is_finger_closed_upside_down(ring_tip, ring_pip, wrist) and
            is_finger_closed_upside_down(pinky_tip, pinky_pip, wrist) and
            not is_touching(thumb_tip, index_tip, index_dip))

def is_letter_r(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)

    handedness = is_right_hand(results, landmarks)

    if handedness: # Right hand
        return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            is_touching(index_tip, middle_tip, middle_dip) and
            index_tip.x < middle_tip.x)
    else: # Left hand
        return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            is_touching(index_tip, middle_tip, middle_dip) and
            index_tip.x > middle_tip.x)

def is_letter_s(results, landmarks):
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    left = min(index_tip.x, index_pip.x, pinky_tip.x, pinky_pip.x)
    right = max(index_tip.x, index_pip.x, pinky_tip.x, pinky_pip.x)
    top = min(index_tip.y, index_pip.y, pinky_tip.y, pinky_pip.y)
    bottom = max(index_tip.y, index_pip.y, pinky_tip.y, pinky_pip.y)
    
    return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            left < thumb_tip.x < right and
            top < thumb_tip.y < bottom)

def is_letter_t(results, landmarks):
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)    
    return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            thumb_tip.x < max(index_pip.x, middle_pip.x) and
            thumb_tip.x > min(index_pip.x, middle_pip.x))

def is_letter_u(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
   
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            is_touching(index_tip, middle_tip, middle_dip) and
            not (thumb_tip.x < max(index_pip.x, middle_pip.x) and
            thumb_tip.x > min(index_pip.x, middle_pip.x)))

def is_letter_v(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            not is_touching(index_tip, middle_tip, middle_dip) and
            not (thumb_tip.x < max(index_mcp.x, middle_mcp.x) and
            thumb_tip.x > min(index_mcp.x, middle_mcp.x)))

def is_letter_w(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_dip = thumb_mcp_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            not is_touching(ring_tip, middle_tip, middle_dip) and
            not is_touching(index_tip, middle_tip, middle_dip) and
            is_touching(pinky_tip, thumb_tip, thumb_dip))

def is_letter_x(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    
    return (is_index_x(index_tip, index_pip, index_mcp) and
            not is_finger_open(middle_tip, middle_pip, wrist) and 
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and
            (is_touching(thumb_tip, middle_pip, middle_dip) or
             is_touching(thumb_tip, middle_dip, middle_pip)))

def is_letter_y(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    if handedness: # Right hand
        #print (normalized_slope(thumb_mcp, thumb_tip))
        return (is_facing_forward(results, landmarks) and
                (normalized_slope(thumb_mcp, thumb_tip) > -.7 and
                normalized_slope(thumb_mcp, thumb_tip) < 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))
    else: # Left hand
        #print (normalized_slope(thumb_mcp, thumb_tip))
        return (is_facing_forward(results, landmarks) and
                (normalized_slope(thumb_mcp, thumb_tip) < .7 and
                normalized_slope(thumb_mcp, thumb_tip) > 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))

def is_letter_z(results, landmarks):
    return False

