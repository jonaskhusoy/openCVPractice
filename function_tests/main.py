##uses erosion and dilution to smooth the contour around the fish

import cv2 as cv
path = "images/klippfisk_demo.jpg"
# legend = "Red: far left \n Green: far right \n Blue: top \n Teal: bottom \n Blue circle: centroid"
# load the image, convert it to grayscale, and blur it slightly
image = cv.imread(path)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5, 5), 0)

# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh1 = cv.threshold(gray, 254, 254, cv.THRESH_BINARY_INV)[1] #invert color to have white foreground for contour
thresh = cv.erode(thresh1, None, iterations=2)
thresh = cv.dilate(thresh, None, iterations=2)
# find contours in thresholded image, then grab the largest
# one

cnts, res = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv.contourArea) #find largest contour (shape of fish)
cnt = cv.drawContours(image, [c], -1, (0,255,0))  # Draw the largest contour in green


#find extreme most left, right, top and bottom points from largest contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

#creates circle around points
cv.circle(image, extLeft, 8, (0, 0, 255), -1)
cv.circle(image, extRight, 8, (0, 255, 0), -1)
cv.circle(image, extTop, 8, (255, 0, 0), -1)
cv.circle(image, extBot, 8, (255, 255, 0), -1)

 #extract centroid of fish contour
M = cv.moments(c)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
centroid = cv.circle(image,(cx, cy), 20, (255,0,0), 2)


# image = cv.putText(image,legend,(cx,cy), 1, 1, (255,0,0), 5)
#display the result image
cv.imshow("contours", image)
cv.imshow("after", thresh)
cv.waitKey()
cv.destroyAllWindows()