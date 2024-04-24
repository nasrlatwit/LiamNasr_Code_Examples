import cv2
import mediapipe as mp

from helpers import *
from letters import *

def main():
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 4
    text_position_left = (10, 80)
    color = (255, 50, 255)
    
    ret, frame = cap.read()
    # height, width = frame.shape[:2]
    # cv2.setWindowProperty("Hand Tracking", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.resizeWindow('Hand Tracking', width, height)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        # If hands are detected, draw landmarks on the frame
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS)
                
                text = ''
                if is_letter_a(results, landmarks):
                    text = 'A'
                elif is_letter_b(results, landmarks):
                    text = 'B'
                elif is_letter_c(results, landmarks):
                    text = 'C'
                elif is_letter_d(results, landmarks):
                    text = 'D'
                elif is_letter_e(results, landmarks):
                    text = 'E'
                elif is_letter_f(results, landmarks):
                    text = 'F'
                elif is_letter_g(results, landmarks):
                    text = 'G'
                elif is_letter_h(results, landmarks):
                    text = 'H'
                elif is_letter_i(results, landmarks):
                    text = 'I'
                elif is_letter_j(results, landmarks):
                    text = 'J'
                elif is_letter_k(results, landmarks):
                    text = 'K'
                elif is_letter_l(results, landmarks):
                    text = 'L'
                elif is_letter_m(results, landmarks):
                    text = 'M'
                elif is_letter_n(results, landmarks):
                    text = 'N'
                elif is_letter_o(results, landmarks):
                    text = 'O'
                elif is_letter_p(results, landmarks):
                    text = 'P'
                elif is_letter_q(results, landmarks):
                    text = 'Q'
                elif is_letter_r(results, landmarks):
                    text = 'R'
                elif is_letter_t(results, landmarks):
                    text = 'T'
                elif is_letter_s(results, landmarks):
                    text = 'S'
                elif is_letter_u(results, landmarks):
                    text = 'U'
                elif is_letter_v(results, landmarks):
                    text = 'V'
                elif is_letter_w(results, landmarks):
                    text = 'W'
                elif is_letter_x(results, landmarks):
                    text = 'X'
                elif is_letter_y(results, landmarks):
                    text = 'Y'
                elif is_letter_z(results, landmarks):
                    text = 'Z'
                
                cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
