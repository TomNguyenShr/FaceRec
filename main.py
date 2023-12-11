from Classes import data_processor, face_detector
from Utils import parse
import cv2
if __name__ == "__main__":
    io = parse.main()
    landmarks = data_processor.Dlib(io[0])
    face_detect = face_detector.Facedetector(io[0])
    face = landmarks.allfacebound()
    lefteyes = landmarks.lefteyes()
    righteyes = landmarks.righteyes()
    cv2.imwrite(io[1], face_detect.facial_rec())


