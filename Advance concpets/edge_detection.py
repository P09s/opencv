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
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)

# canny is more advance algorithm compares to sobel
canny = cv.Canny(gray, 150, 175)

cv.imshow('soble x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('combined', combined)
cv.imshow('canny', canny)

cv.waitKey(0)