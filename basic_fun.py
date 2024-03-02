import cv2 as cv
import numpy as np

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

# converting image to gray color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('bro', gray)

# blurring the image to gray
blur = cv.GaussianBlur(img, (15,15), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edges cascading - finding edges of the image
canny = cv.Canny(img, 125, 175)
cv.imshow('canny img', canny)

# dilating the edges
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated image', dilated)

# eroding the dilation and getting the canny 
eroded = cv.erode(dilated, (3,3), iterations=4)
cv.imshow('eroded', eroded)

# resize the image
resize = cv.resize(img, )

cv.waitKey(0)