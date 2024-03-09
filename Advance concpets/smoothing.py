import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

# averaging in image
avg = cv.blur(img, (7,7))
cv.imshow('average', avg)

# gaussian blur (it is more natural looking as compare to the blur by using average)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss', gauss)

median = cv.medianBlur(img, 7)
cv.imshow('medain', median)
cv.waitKey(0)