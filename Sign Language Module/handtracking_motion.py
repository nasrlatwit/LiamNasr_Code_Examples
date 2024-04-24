import cv2
import mediapipe as mp

from collections import deque
from helpers import *
from letters import *

import numpy as np

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, estimated_measurement_variance):
        self.process_variance = process_variance
        self.measurement_variance = measurement_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 0.0
        self.posteri_error_estimate = 1.0

    def update(self, measurement):
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        blending_factor = priori_error_estimate / (priori_error_estimate + self.estimated_measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

        return self.posteri_estimate

def detect_z(index_hand_landmarks):
    # Filter out None values
    index_hand_landmarks = [point for point in index_hand_landmarks if point[0] is not None and point[1] is not None]

    # Check if there are enough points to analyze
    if len(index_hand_landmarks) < 7:
        return False, []

    # Apply Kalman filter to smooth hand landmark positions
    kf_x = KalmanFilter(process_variance=1e-5, measurement_variance=0.1, estimated_measurement_variance=0.1)
    kf_y = KalmanFilter(process_variance=1e-5, measurement_variance=0.1, estimated_measurement_variance=0.1)
    
    smoothed_landmarks = []
    for point in index_hand_landmarks:
        smoothed_x = kf_x.update(point[0])
        smoothed_y = kf_y.update(point[1])
        smoothed_landmarks.append((smoothed_x, smoothed_y))

    # Extract x and y coordinates of the smoothed points
    # x_values = [point[0] for point in smoothed_landmarks]
    # y_values = [point[1] for point in smoothed_landmarks]
    x_values = [point[0] for point in index_hand_landmarks]
    y_values = [point[1] for point in index_hand_landmarks]

    # Find corners (significant changes in direction)
    corners = []
    corner_indecies = []
    for i in range(3, len(smoothed_landmarks) - 3):
        dx1 = x_values[i] - x_values[i-3]
        dy1 = y_values[i] - y_values[i-3]
        dx2 = x_values[i] - x_values[i+3]
        dy2 = y_values[i] - y_values[i+3]
        if (dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5 != 0.0: # Avoid division by zero
            angle = (dx1*dx2 + dy1*dy2) / ((dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5)
            try:
                angle_degrees = math.degrees(math.acos(angle))
            except Exception as e:
                angle_degrees = 180
            if angle_degrees < 70 and (len(corner_indecies) == 0 or i - corner_indecies[-1] > 2):
                corners.append((x_values[i], y_values[i]))
                corner_indecies.append(i)

    # Check if corners form the shape of a 'Z'
    if len(corners) > 2:
        start = (x_values[0], y_values[0])
        end = corners[2]#(x_values[-1], y_values[-1])
        first_corner = corners[0]
        last_corner = corners[1]

        # Check if corners are aligned with the start and end points
        if (start[0] > first_corner[0] and start[0] > end[0] and
            start[1] < end[1] and start[1] < last_corner[1] and
            
            first_corner[0] < last_corner[0] and
            first_corner[1] < end[1] and last_corner[1] and
            
            last_corner[0] > end[1]):
            return True, corners

    return False, corners

def detect_j(pinky_hand_landmarks):
    # Filter out None values
    pinky_hand_landmarks = [point for point in pinky_hand_landmarks if point[0] is not None and point[1] is not None]

    # Check if there are enough points to analyze
    if len(pinky_hand_landmarks) < 7:
        return False, []

    # Apply Kalman filter to smooth hand landmark positions
    kf_x = KalmanFilter(process_variance=1e-5, measurement_variance=0.1, estimated_measurement_variance=0.1)
    kf_y = KalmanFilter(process_variance=1e-5, measurement_variance=0.1, estimated_measurement_variance=0.1)
    
    smoothed_landmarks = []
    for point in pinky_hand_landmarks:
        smoothed_x = kf_x.update(point[0])
        smoothed_y = kf_y.update(point[1])
        smoothed_landmarks.append((smoothed_x, smoothed_y))

    # Extract x and y coordinates of the smoothed points
    # x_values = [point[0] for point in smoothed_landmarks]
    # y_values = [point[1] for point in smoothed_landmarks]
    x_values = [point[0] for point in pinky_hand_landmarks]
    y_values = [point[1] for point in pinky_hand_landmarks]

    # Find curve (smooth changes in direction)
    curves = []
    curves_indecies = []
    for i in range(3, len(smoothed_landmarks) - 3):
        dx1 = x_values[i] - x_values[i-3]
        dy1 = y_values[i] - y_values[i-3]
        dx2 = x_values[i] - x_values[i+3]
        dy2 = y_values[i] - y_values[i+3]
        if (dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5 != 0.0: # Avoid division by zero
            angle = (dx1*dx2 + dy1*dy2) / ((dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5)
            try:
                angle_degrees = math.degrees(math.acos(angle))
            except Exception as e:
                angle_degrees = 180
            if angle_degrees < 70 and (len(curves_indecies) == 0 or i - curves_indecies[-1] > 2):
                curves.append((x_values[i], y_values[i]))
                curves_indecies.append(i)

    # Check if curves form the shape of a 'Z'
    if len(curves) > 1:
        start = (x_values[0], y_values[0])
        end = curves[1]#(x_values[-1], y_values[-1])
        first_curve = curves[0]

        # Check if curves are aligned with the start and end points
        if (start[0] < first_curve[0] and start[1] < first_curve[1] and
            first_curve[0] < end[0] and start[1] < end[1]):

            return True, curves

    return False, curves

def main():
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 4
    text_position_left = (10, 80)
    color = (255, 50, 255)

    # Queue to store locations of index and pinky finger tips for the last 150 frames
    index_finger_tip_locations = deque(maxlen=50)
    pinky_finger_tip_locations = deque(maxlen=50)
    
    hold_z = 0
    hold_j =0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        # If hands are detected, draw landmarks on the frame and store index finger tip location
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

                # Get index finger tip location
                index_finger_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                image_height, image_width, _ = frame.shape
                index_finger_tip_x = int(index_finger_tip.x * image_width)
                index_finger_tip_y = int(index_finger_tip.y * image_height)

                # Get pinky finger tip location
                pinky_finger_tip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_TIP]
                image_height, image_width, _ = frame.shape
                pinky_finger_tip_x = int(pinky_finger_tip.x * image_width)
                pinky_finger_tip_y = int(pinky_finger_tip.y * image_height)

                # Store index and pinky finger tips location
                index_finger_tip_locations.append((index_finger_tip_x, index_finger_tip_y))
                pinky_finger_tip_locations.append((pinky_finger_tip_x, pinky_finger_tip_y))
        else:
            index_finger_tip_locations.append((None, None))
            pinky_finger_tip_locations.append((None, None))

        # Draw index finger tip locations from the last 50 frames
        for x, y in index_finger_tip_locations:
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        # Draw pinky finger tip locations from the last 50 frames
        for x, y in pinky_finger_tip_locations:
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            
        text = ''
        
        z_found, corners = detect_z(index_finger_tip_locations)
        j_found, curves = detect_j(pinky_finger_tip_locations)
        
        if z_found or hold_z > 0:
            text = 'Z'
            hold_z += 1
            
        if hold_z == 0 or hold_z == 50:
            hold_z = 0
            
        for corner in corners:
            cv2.circle(frame, (int(corner[0]), int(corner[1])), 7, (0, 0, 255), -1)


        if j_found or hold_j > 0:
            text = 'J'
            hold_j += 1
            
        if hold_j == 0 or hold_j == 50:
            hold_j = 0
            
        for curve in curves:
            cv2.circle(frame, (int(curve[0]), int(curve[1])), 7, (0, 0, 255), -1)
        
        cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()