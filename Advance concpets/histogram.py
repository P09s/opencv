import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale histograms')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.show()

cv.waitKey(0)