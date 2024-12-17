# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:41:50 2024

@author: Lenovo
"""

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from matplotlib.colors import NoNorm

o = io.imread("images/Fractured/51.png")
 #Apply log transformation method
 
c = 255/(np.log(1+255))
inv_log_image = np.exp(o**1/c)-1
inv_log_image = np.array(inv_log_image, dtype=np.uint8)

plt.figure(figsize=(15, 4))
plt.subplot(1, 3, 1)
plt.imshow(o, cmap='gray', norm=NoNorm())
plt.subplot(1, 3, 2)
plt.imshow(inv_log_image, cmap='gray', norm=NoNorm())
plt.show()

