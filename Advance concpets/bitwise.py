import cv2 as cv
import numpy as np

# img = cv.imread('Photos/bro.jpg')
# cv.imshow('bro', img)

blank = np.zeros((400,400), dtype = 'uint8' )
cv.imshow('blank', blank)

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cir = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rect)
cv.imshow('circle', cir)

# bitwise AND
bitwise_and = cv.bitwise_and(rect, cir)
cv.imshow('bitwise and', bitwise_and)

# bitwise or
bitwise_or = cv.bitwise_or(rect, cir)
cv.imshow('bitwise or', bitwise_or)

# bitwise xor
bitwise_xor = cv.bitwise_xor(rect, cir)
cv.imshow('bitwise xor', bitwise_xor)

# bitwise not
bitwise_not = cv.bitwise_not( cir)
cv.imshow('bitwise not', bitwise_not)

cv.waitKey(0)