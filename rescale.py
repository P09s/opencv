import cv2 as cv

img = cv.imread('Photos/2023-03-05.png')
cv.imshow('2023-03-05', img)

def rescaleFrame(frame, scale = 0.75) :
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# rescale or reize the image to be adjusted on screen

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('videos/ar filter demo.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('videos', frame)
    cv.imshow('videos Resized', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()