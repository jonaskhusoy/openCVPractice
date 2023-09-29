#the goal here is to implement the same functions as in main.py, however the background is more like the actual prod environment with more challenging nuances and colors.

##this one uses masking and HSV to extract color hues
import cv2 as cv
import numpy as np

PATH = "C://OpenCV/src/images/fish_gray_background.PNG"
img = cv.imread(PATH) #original img
result = img.copy() #img to operate on


# cropped = img[300:2000, 150:1200] #create a ROI to filter out uncessary background and noise and get a more uniform background. In prod only background will be gray so this will not be needed

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, (0,0,0),(20,45,255)) #gray filter
thresh = cv.bitwise_not(mask) #invert to get white foreground (fish)

#clean up the contour and remove some noise
thresh = cv.erode(thresh, None, iterations=3)
thresh = cv.dilate(thresh, None, iterations=2)
thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, (5,5))


# find only largest contour from findContours function
cnts, res = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv.contourArea) #find largest contour (shape of fish)
cnt = cv.drawContours(img, [c], -1, (0,255,0))  # Draw the largest contour in green




#find extreme most left, right, top and bottom points from largest contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

#creates circle around points
cv.circle(img, extLeft, 8, (0, 0, 255), -1)
cv.circle(img, extRight, 8, (0, 255, 0), -1)
cv.circle(img, extTop, 8, (255, 0, 0), -1)
cv.circle(img, extBot, 8, (255, 255, 0), -1)

 #extract centroid of fish contour
M = cv.moments(c)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
centroid = cv.circle(img,(cx, cy), 20, (255,0,0), 2)




#display both original img and modified img
cv.imshow("1", mask)
cv.imshow("2", img)
# cv.imshow("3", mask3)

cv.waitKey()
cv.destroyAllWindows()
