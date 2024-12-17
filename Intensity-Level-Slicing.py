# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:21:30 2024

@author: Lenovo
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def binary_slicing(image,A,B,lower_value,upper_value):
    image_output = np.full_like(image, lower_value)
    index = np.logical_and(image > A, image < B)
    image_output[index] = upper_value
    return image_output


def linear_slicing(image,A,B,value):
    image_output = image.copy()
    index = np.logical_and(image > A, image < B)
    image_output[index] = value
    return image_output



image = cv2.imread("images/Fractured/47.png",0)


binary_img = binary_slicing(image,50,100,10,255)
linear_img = linear_slicing(image, 50, 100, 255)
    


image = cv2.resize(image, (400,400))
binary_img = cv2.resize(binary_img, (400,400))
linear_img = cv2.resize(linear_img, (400,400))

horizontal_img = np.hstack((image,linear_img))
cv2.imshow("Orginal Image vs Gamma Image ",horizontal_img)
cv2.waitKey(0)
cv2.destroyAllWindows()