import cv2
import os


def capturePicture(camera_index=0, name='capturedImage.jpg'):
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
