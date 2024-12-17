# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:38:23 2024

@author: Lenovo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



def power_law_gamma_transformations(c, r, gamma):
    r = r.astype(float)
    s = c*r**gamma
    s = rescale(s)
    return s


def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

image = cv2.imread("images/Fractured/138.png",0)
power_law_img = power_law_gamma_transformations(1, image, 0.4)
    

image = cv2.resize(image, (400,400))
power_law_img = cv2.resize(power_law_img, (400,400))


horizontal_img = np.hstack((image,power_law_img))
cv2.imshow("Orginal Image vs Gamma Image ",horizontal_img)

cv2.waitKey(0)
cv2.destroyAllWindows()