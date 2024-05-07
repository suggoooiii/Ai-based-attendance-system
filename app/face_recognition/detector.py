# app/face_recognition/detector.py
import cv2

class FaceDetector:
    def __init__(self, cascade_path):
        self.cascade = cv2.CascadeClassifier(cascade_path)

    def detect_faces(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        return faces
