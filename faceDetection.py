# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 16:03:20 2018
@author: Rajprakash.Bale
"""
import cv2, dlib

def imageProcess(image):
    img = cv2.imread(image)                             # read the input image
    r = 1500.0 / img.shape[1]                           # resize the image 
    dim = (1500, int(img.shape[0] * r))
    image_cv = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    detector = dlib.get_frontal_face_detector()
    dets = detector(image_cv,1)
    return len(dets)
    

if __name__ == '__main__':
    image_path = "path of the image"
    no_of_faces = imageProcess(image_path)
    print(no_of_faces)