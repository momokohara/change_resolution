# !/usr/bin/python

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def scale_to_resolation(img, resolation):
        """指定した解像度になるように、アスペクト比を固定して、リサイズする。"""
        h, w = img.shape[:2]
        print(h, w)
        scale = (resolation / (w * h)) ** 0.5
        return cv2.resize(img, dsize=None, fx=scale, fy=scale)

img_array = cv2.imread("test.png")
img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
print(img_array.shape)

resize = scale_to_resolation(img_array, 64 * 48)

print(resize.shape)
plt.subplot(121).imshow(img_array)
plt.subplot(122).imshow(resize)

plt.show()
