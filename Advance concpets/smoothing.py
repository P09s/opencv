import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

# averaging in image
avg = cv.blur(img, (3,3))
cv.imshow('average', avg)

cv.waitKey(0)