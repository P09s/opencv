import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

## Grayscale histogram

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale histograms')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.show()

## colored histogram

plt.figure()
plt.title('Colored histograms')
plt.xlabel('bins')
plt.ylabel('# of pixels')

color = ['b', 'g', 'r']
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)