import cv2
import os


def capturePicture(name='capturedImage.jpg'):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
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


capturePicture()
