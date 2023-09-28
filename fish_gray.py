import cv2 as cv
import numpy as np

path = "C:\OpenCV\images\klippfisk_demo.jpg" #img path

img = cv.imread(path) #cv img object

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert color scheme to HSV for easier color separation

ret, mask = cv.threshold(img_gray, 250, 255, cv.THRESH_BINARY)

cv.imshow("frame", mask)
k = cv.waitKey(0)
cv.destroyAllWindows

result = img_gray.copy() #new image to create contours on
result = 255-result

contours, hierachy = cv.findContours(result, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# Sort the contours by area in descending order
contours = sorted(contours, key=cv.contourArea, reverse=True)

# Select the largest contour (the first contour in the sorted list)
largest_contour = contours[0]


cv.drawContours(img, [largest_contour], -1, (0,255,0))  # Draw the largest contour in green


cv.imshow("frame", img)
k = cv.waitKey(0)
cv.destroyAllWindows
print(len(contours))



