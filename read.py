import cv2 as cv

# # read image
# img = cv.imread('Photos/2023-03-05.png')

# # display image
# cv.imshow('2023-03-05', img)

# cv.waitKey(0)

# read videos 
capture = cv.VideoCapture('videos/ar filter demo.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('videos', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()