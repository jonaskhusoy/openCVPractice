import cv2 as cv
import numpy as np

path = "C:\OpenCV\images\klippfisk_demo.jpg" #img path

img = cv.imread(path) #cv img object

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert color scheme to HSV for easier color separation

ret, mask = cv.threshold(img_gray, 250, 255, cv.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)

cv.imshow("frame", mask)
k = cv.waitKey(0)
cv.destroyAllWindows

result = img_gray.copy() #new image to create contours on
result = cv.bitwise_not(mask)

contours, hierachy = cv.findContours(result, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Sort the contours by area in descending order
contours = sorted(contours, key=cv.contourArea, reverse=True)

# Select the largest contour (the first contour in the sorted list)
largest_contour = contours[0]
contour_area = cv.contourArea(largest_contour)
print(contour_area," is area of fish.")

cv.drawContours(img, [largest_contour], -1, (0,255,0))  # Draw the largest contour in green
#display original image with contours
cv.imshow("frame", img)
k = cv.waitKey(0)
cv.destroyAllWindows
print(len(contours))


#next step: find corners

 #rotate to easier use pixels to find points. from center of image or center of fish?
 
 
 #implement contouring on video
 #adaptive thresholding?
 #blurring to smooth edges of contour?
 
 
 #extract centroid of fish contour
M = cv.moments(largest_contour)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

centroid = cv.circle(img,(cx, cy), 20, (255,0,0), 2)
cv.imshow("centroid" , centroid)
cv.waitKey()
cv.destroyAllWindows()




