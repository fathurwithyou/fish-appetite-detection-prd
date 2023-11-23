import cv2
import os


def capture_picture(camera_index=0, name='capturedImage.jpg', width=640, height=480):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open the camera")
        return

    try:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture a frame.")
            return

        cv2.imwrite('imgTest/'+name, frame)
        print(f"Image saved as {name}")
        
    finally:
        cap.release()
    return name
