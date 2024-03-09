import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro',img )

# BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR TO HSV( hue sauration value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
cv.imshow('hsv', hsv)

# BGR to Lab (L*a*b)
Lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', Lab)

cv.waitKey(0)