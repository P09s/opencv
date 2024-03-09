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

# rotation

def rotate(img, angle, rotpoint=None) :
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions) 
rotated = rotate(img, 180)
cv.imshow('Rotated image', rotated)

# flip image

flipped = cv.flip(img, -1)
cv.imshow('Flipped image', flipped)

# cropped image

cropping = img[200:400, 300:400]
cv.imshow("cropped", cropping)
cv.waitKey(0)
