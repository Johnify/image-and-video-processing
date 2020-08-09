# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:41:53 2020

@author: USER
"""
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('IM2TEXT.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

### Detecting words
hImg, wImg, X = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)
#for b in boxes.splitlines():
    #print(b )
   # b = b.split(' ')
   # print(b)
   # x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
   # cv2.rectangle(img, (x, hImg-y), (x+w, hImg-h), (0, 0, 255), 0)
   # cv2.putText(img, b[0], (x, hImg-y), cv2.FONT_HERSHEY_COMPLEX,1, (50,50,255))


cv2.imshow('IM2TEXT', img)
cv2.waitKey(0)