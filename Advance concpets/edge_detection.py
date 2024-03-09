import cv2 as cv
import numpy as np

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro',img )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian
lap = cv.Laplacian ( gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap', lap)

# sobel

cv.waitKey(0)