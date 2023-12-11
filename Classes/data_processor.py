import cv2 
import dlib
import numpy as np

class Dlib:
    def __init__(self, imgrgb):
        self.imgrgb = cv2.imread(imgrgb) 
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def allfacebound(self):
        face = self.detector(self.imgrgb, 1)
        print(f"Face: x = {face[0].left()} y = {face[0].top()}, height = {face[0].height()}, width = {face[0].width()}")

    def lefteyes(self):
        face = self.detector(self.imgrgb, 1)
        landmarks = self.predictor(self.imgrgb, face[0])
        left_eyes = list(range(42, 48))
        left_eyes_x = [landmarks.part(i).x for i in left_eyes]
        left_eyes_y = [landmarks.part(i).y for i in left_eyes]
        width = max(left_eyes_x)-min(left_eyes_x)
        height = max(left_eyes_y)-min(left_eyes_y)
        print(f"Lefteye: x = {max(left_eyes_x)} y = { max(left_eyes_y)}, height = {height}, width = {width}")
    
    def righteyes(self):
        face = self.detector(self.imgrgb, 1)
        landmarks = self.predictor(self.imgrgb, face[0])
        right_eyes = list(range(36, 42))
        right_eyes_x = [landmarks.part(i).x for i in right_eyes]
        right_eyes_y = [landmarks.part(i).y for i in right_eyes]
        width = max(right_eyes_x)-min(right_eyes_x)
        height = max(right_eyes_y)-min(right_eyes_y)
        print(f"Righteye: x = {max(right_eyes_x)} y = { max(right_eyes_y)}, height = {height}, width = {width}")
        
        
