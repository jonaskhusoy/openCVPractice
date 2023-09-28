import cv2 as cv
import numpy as np
import os

img_path = "klippfisk_demo.jpg"
new_img_path = "opencv_logo.png"

path = "C:/OpenCV/new_image.jpg"

img = cv.imread(img_path)
img2 = cv.imread(new_img_path)



    #roi is the size and location of img2 inside img 1.
rows, cols, channel = img2.shape
roi = img[0:rows, 0:cols] 
 


# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY) #convert to gray
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY) #converts to black and white
mask_inv = cv.bitwise_not(mask) #inverse logo
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv) #roi from img1, only logo from img2
 # Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2)
img[0:rows, 0:cols ] = dst

cv.imshow('res',img)
cv.imshow("img_bg", img1_bg)
cv.imshow("img2_fg", img2_fg)
cv.imshow("mask", mask)
cv.imshow("mask_inv", mask_inv) 
cv.imshow("org", img2)
cv.waitKey(0)
cv.destroyAllWindows()

