#!/bin/python
# fileUsing: use threshold value T to binary image

import cv2
from matplotlib import pyplot as plt

image = cv2.imread("img/2-1.png")
# 将输入图像转为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 绘制灰度图
plt.subplot(121), plt.imshow(gray, "gray")
plt.title("input image"), plt.xticks([]), plt.yticks([])

# 对灰度图使用 全局阈值 算法
h, w = gray.shape

T = 100  # set threshold value
for y in range(w):
    for x in range(h):
        if gray[x][y] < T:
            gray[x][y] = 0
        else:
            gray[x][y] = 255

# 绘制阈值图
plt.subplot(122), plt.imshow(gray, "gray")
plt.title("thread image"), plt.xticks([]), plt.yticks([])
plt.show()