import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('img', img)

b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)