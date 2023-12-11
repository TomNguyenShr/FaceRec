import cv2
import dlib

class Facedetector():
    def __init__(self, imgrgb):
        self.imgrgb = cv2.imread(imgrgb) 
        self.detector = dlib.get_frontal_face_detector()

    def facial_rec(self):
        faces = self.detector(self.imgrgb, 1)

        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(self.imgrgb, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return self.imgrgb

# align_dlib = Facedetector("lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")
# align_dlib.facial_rec()