import mediapipe as mp
import numpy as np
from hand_landmarks import *
import math

def is_hand_open(landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = wrist_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    # Check if each induvidual finger is open
    index_open = is_finger_open(index_tip, index_pip, wrist)
    middle_open = is_finger_open(middle_tip, middle_pip, wrist)
    ring_open = is_finger_open(ring_tip, ring_pip, wrist)
    pinky_open = is_finger_open(pinky_tip, pinky_pip, wrist)

    return index_open and middle_open and ring_open and pinky_open

def is_hand_closed(landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = wrist_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    # Check if each induvidual finger is closed
    index_closed = not is_finger_open(index_tip, index_pip, wrist)
    middle_closed = not is_finger_open(middle_tip, middle_pip, wrist)
    ring_closed = not is_finger_open(ring_tip, ring_pip, wrist)
    pinky_closed = not is_finger_open(pinky_tip, pinky_pip, wrist)

    return index_closed and middle_closed and ring_closed and pinky_closed

def is_hand_closed_sideways(results, landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = wrist_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    handedness = is_right_hand(results, landmarks)

    # Check if each induvidual finger is closed
    if handedness:
        index_closed = normalized_slope(index_tip, index_pip) > -0.5
        middle_closed = normalized_slope(middle_tip, middle_pip) > -0.4
        ring_closed = normalized_slope(ring_tip, ring_pip) > -0.3
        pinky_closed = normalized_slope(pinky_tip, pinky_pip) > -0.3
    else:
        index_closed = normalized_slope(index_tip, index_pip) < 0.5
        middle_closed = normalized_slope(middle_tip, middle_pip) < 0.4
        ring_closed = normalized_slope(ring_tip, ring_pip) < 0.3
        pinky_closed = normalized_slope(pinky_tip, pinky_pip) < 0.3
    
    return index_closed and middle_closed and ring_closed and pinky_closed

def is_finger_open(finger_tip, finger_pip, wrist):
    if wrist.y < finger_pip.y:
        return finger_tip.y > finger_pip.y
    else:
        return finger_tip.y < finger_pip.y
    

def is_right_hand(results, landmarks):
    return results.multi_handedness[
                results.multi_hand_landmarks.index(landmarks)
            ].classification[0].label == 'Left'
    
def distance(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def normalized_slope(a, b):
    '''
    Gives a normalized slope from 0 - 1, 0 being horizontal and 1 being vertical.
    A negative slope is given for negative slopes which can be used to distiguish
    between left and right hand positions
    '''
    if a.x == b.x:
       return 1
    slope_value = (a.y - b.y) / (a.x - b.x)
    return math.atan(slope_value) / (math.pi / 2)

def is_touching(finger1_tip, finger2_tip, finger2_dip):
    return distance(finger1_tip, finger2_tip) < distance(finger2_tip, finger2_dip) * 1.25

def is_facing_forward(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    
    thumb_cmc = thumb_cmc_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    middle_mcp = middle_mcp_lm(landmarks)
    ring_mcp = ring_mcp_lm(landmarks)
    pinky_mcp = pinky_mcp_lm(landmarks)
    
    if handedness:
        return (pinky_mcp.x < ring_mcp.x < middle_mcp.x < index_mcp.x and 
                thumb_cmc.y > thumb_mcp.y and
                distance(index_mcp, pinky_mcp) > distance(index_mcp, wrist) / 3)
    else:
        return (pinky_mcp.x > ring_mcp.x > middle_mcp.x > index_mcp.x  and 
                thumb_cmc.y > thumb_mcp.y and
                distance(index_mcp, pinky_mcp) > distance(index_mcp, wrist) / 3)
        
def is_facing_back_and_sideways(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    middle_mcp = middle_mcp_lm(landmarks)
    ring_mcp = ring_mcp_lm(landmarks)
    pinky_mcp = pinky_mcp_lm(landmarks)
    
    if handedness:
        return (pinky_mcp.y > ring_mcp.y > middle_mcp.y > index_mcp.y and
                abs(normalized_slope(pinky_mcp, index_mcp)) > 0.4 and
                index_mcp.x > wrist.x)
    else:
        return (pinky_mcp.y > ring_mcp.y > middle_mcp.y > index_mcp.y and
                abs(normalized_slope(pinky_mcp, index_mcp)) > 0.4 and
                index_mcp.x < wrist.x)
    
def is_finger_open_sideways(finger_tip, finger_pip, handedness):
    if handedness:
        return finger_tip.x > finger_pip.x
    else:
        return finger_tip.x < finger_pip.x
    
def is_index_x(index_tip, index_pip, index_mcp):
    return (normalized_slope(index_tip, index_pip) < .5 and
            normalized_slope(index_tip, index_pip) > -.5 and
            (normalized_slope(index_mcp, index_pip) > 0.7 or
            normalized_slope(index_mcp, index_pip) < -0.7))
    
def is_finger_closed_upside_down(finger_tip, finger_pip, wrist):
    return wrist.y < finger_tip.y < finger_pip.y