import cv2 as cv
import numpy as np

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

## firstly use canny method for contour detection, then try using thresh since thresh fails sometime !!

# canny = cv.Canny(blur, 125, 125)
# cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 225, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contour, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} contour(s) found !' )

cv.drawContours(blank, contour, -1, (0,0,255), 1)
cv.imshow('draw contour',blank)

cv.waitKey(0)