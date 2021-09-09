#!/usr/bin/python

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

img_array = np.array([[0,1,1,1,1,1,1,1,1,1],
			[1,0,1,1,1,1,1,1,1,1],
			[1,1,0,1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1,1,1,1],
			[1,1,1,1,0,1,1,1,1,1],
			[1,1,1,1,1,0,1,1,1,1],
			[1,1,1,1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1,0,1,1],
			[1,1,1,1,1,1,1,1,0,1],
			[1,1,1,1,1,1,1,1,1,0]]).astype('float64')

print(img_array)
print(img_array.shape)

# pil = Image.fromarray(np.uint8(img_array))

resize = scale_to_resolation(img_array, 2 * 2)

# resize = np.asarray(dst) 
print(resize)
print(resize.shape)
plt.subplot(121).imshow(img_array, cmap = plt.cm.binary_r)
plt.subplot(122).imshow(resize, cmap = plt.cm.binary_r)

plt.show()
