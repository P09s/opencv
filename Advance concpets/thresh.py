import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro',img )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresholded image', thresh)

# inversing blank and white color in thresh
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded inverse image', thresh_inv)


cv.waitKey(0)