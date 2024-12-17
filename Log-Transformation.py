# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:13:23 2024

@author: Lenovo
"""

import cv2
import numpy as np

def log_transformation(c,r):
    r = r.astype(float)
    s = c * np.log( 1 + r )
    return s.astype(np.uint8)


def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

img = cv2.imread("images/Fractured/47.png",0)
log_image = log_transformation(1, img)
log_image = rescale(log_image)


img = cv2.resize(img, (400,400))
log_image = cv2.resize(log_image, (400,400))

horizontal_img = np.hstack((img,log_image))
cv2.imshow("Orginal Image vs Log Image ",horizontal_img)
cv2.waitKey(0)
cv2.destroyAllWindows()