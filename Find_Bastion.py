
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:47:37 2021

@author: Jason
"""
# https://medium.com/analytics-vidhya/finding-waldo-feature-matching-for-opencv-9bded7f5ab10

import cv2
import numpy as np
from matplotlib import pyplot as plt

#import images
img_rgb = cv2.imread('Find_Bastion.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('Bastion.png',0)

# resize images
template = cv2.resize(template, (0,0), fx=0.5, fy=0.5)     
img_gray = cv2.resize(img_gray, (0,0), fx=0.5, fy=0.5)
img_rgb  = cv2.resize(img_rgb, (0,0), fx=0.5, fy=0.5)

#Show images
cv2.imshow('This is Bastion',template)
cv2.waitKey(0)
cv2.destroyAllWindows()

     
cv2.imshow('We look for Bastion in this image',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()





# saves the width and height of the template into 'w' and 'h'
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
# finding the values where it exceeds the threshold
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    #draw rectangle on places where it exceeds threshold
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

cv2.imwrite('found_bastion.png',img_rgb)


cv2.imshow('Found that bastion!',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()