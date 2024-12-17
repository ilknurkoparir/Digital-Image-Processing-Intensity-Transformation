# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:48:03 2024

@author: Lenovo
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def bit_plane_slicing(img, bit_duzlemi):
    bit_foto = np.full_like(img, 2**bit_duzlemi)
    return np.bitwise_and(img, bit_foto)
    

def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)


    


image = cv2.imread("images/Fractured/3.png",0)

bit_planes = []
for bit_plane in range(8):
    bit_img = bit_plane_slicing(image, bit_plane)
    bit_img = rescale(bit_img)
    bit_planes.append(bit_img)
    
bit_planes_image = bit_planes[::-1]

h1 = np.hstack((image, bit_planes_image[0], bit_planes_image[1]))
h2 = np.hstack((bit_planes_image[2], bit_planes_image[3], bit_planes_image[4]))
h3 = np.hstack((bit_planes_image[5], bit_planes_image[6], bit_planes_image[7]))

grid = np.vstack((h1,h2,h3))

plt.imshow(grid, cmap="gray")
plt.show()

