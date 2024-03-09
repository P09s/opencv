import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('img', img)

cv.waitKey(0)