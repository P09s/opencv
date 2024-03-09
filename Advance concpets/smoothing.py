import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

# averaging in image
avg = cv.blur(img, (7,7))
cv.imshow('average', avg)

# gaussian blur (it is more natural looking as compare to the blur by using average)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss', gauss)

# median blurrring
median = cv.medianBlur(img, 7)
cv.imshow('medain', median)

# bilateral blurring (most effective and used in mutltiple advance CV project cause it retains the the edges and dosen't remove them)
bilateral = cv.bilateralFilter(img, 7, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)