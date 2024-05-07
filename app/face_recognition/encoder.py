# app/face_recognition/encoder.py
import face_recognition

class FaceEncoder:
    def encode_face(self, image):
        face_encodings = face_recognition.face_encodings(image)
        return face_encodings[0] if face_encodings else None
