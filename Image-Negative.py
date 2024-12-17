# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:29:06 2024

@author: Lenovo
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


def image_negative(img):
    L = np.max(img)
    img_negative = L- img
    return img_negative

img = cv2.imread("images/Fractured/1.png",0)
img_neg = image_negative(img)

img = cv2.resize(img, (400,400))
img_neg = cv2.resize(img_neg, (400,400))

horizontal_img = np.hstack((img,img_neg))
cv2.imshow("Orginal Image vs Negative Image ",horizontal_img)
cv2.waitKey(0)
cv2.destroyAllWindows()