import cv2 as cv
import numpy as np

path = "C:\OpenCV\images\klippfisk_demo.jpg" #img path

img = cv.imread(path) #cv img object

# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert color scheme to HSV for easier color separation

# ret, mask = cv.threshold(img_gray, 250, 255, cv.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow("outline",gradient)
cv.waitKey()
cv.destroyAllWindows