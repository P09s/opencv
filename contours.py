import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(gray, 125, 125)
cv.imshow('canny', canny)

contour, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} contour(s) found !' )

cv.waitKey(0)