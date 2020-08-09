# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:10:13 2019

@author: USER
"""

import cv2
import glob

images = glob.glob("*.jpg") #finds all images with  jpg extension and saves them to images

for image in images:
    img=cv2.imread(image, 0) #reads image as grayscale and stores it to img
    re=cv2.resize(img, (300, 300)) #resizes img to 200*200
    cv2.imshow("Hey", re) 
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re)