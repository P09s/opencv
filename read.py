import cv2 as cv

# read image
img = cv.imread('Photos/2023-03-05.png')

# display image
cv.imshow('2023-03-05', img)

cv.waitKey(0)