import cv2 as cv
import numpy as np

# a blank image
blank = np.zeros((500, 500, 3) , dtype= 'uint8' )
# cv.imshow('blank', blank)

# # 1. paint the image
# blank [200:300 , 300:400] = 0,255,0
# cv.imshow('Green', blank)

# 2. shapes over image
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank )

cv.circle(blank, (250,250), 40, (0,0,255), thickness=3 )
cv.imshow('circle', blank)

cv.line(blank, (0,0), (250,250), (255,0,0), thickness=3 )
cv.imshow('line', blank)

cv.text()

cv.waitKey(0)