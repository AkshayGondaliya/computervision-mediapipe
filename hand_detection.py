import time
import cv2
import mediapipe as mp

cap=cv2.videocapture("")

while True:

    success,frame=cap.read()
    if frame:
        
