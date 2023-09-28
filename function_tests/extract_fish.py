import cv2 as cv
import numpy as np

path = "C:\OpenCV\klippfisk_demo.jpg" #img path

img = cv.imread(path) #cv img object

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) #convert color scheme to HSV for easier color separation

#set range of gray colors on fish
lower_gray = np.array([40,3,47])
higher_gray = np.array([72,2,82])


mask = cv.inRange(img_hsv, lower_gray, higher_gray, ) #extract colors from hsv image

res = cv.bitwise_and(img, img, mask= mask)

cv.imshow('frame',img)
cv.imshow('mask',mask)
cv.imshow('res',res)

k = cv.waitKey(0)
cv.destroyAllWindows

