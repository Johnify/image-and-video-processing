# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:56:41 2019

@author: USER
"""

import cv2

img = cv2.imread("galaxy.jpg", 0) #0 for grayscale

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) #sets the delay to 2secs
cv2.destroyAllWindows() #closes after set time, if time is 0 closes when user presses any BUTTON