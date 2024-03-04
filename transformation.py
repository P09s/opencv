import cv2 as cv
import numpy as np

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

# translation of image

def translate(img, x, y):
    transMatrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

# -x --> left
# -y --> up
#  x --> right
#  y --> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

cv.waitKey(0)
