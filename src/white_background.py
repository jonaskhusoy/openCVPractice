##uses erosion and dilution to smooth the contour around the fish
import cv2 as cv
import util.util
# PATH = "C://OpenCV/src/images/klippfisk_demo.jpg"
PATH = "C://OpenCV/src/images/fish_gray_background.PNG"


# load the image, convert it to grayscale, and blur it slightly in order to prepare for next step
image = cv.imread(PATH)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5, 5), 0)

# threshold the image, then perform a series of erosions and dilutions to smooth the outline of the contour
thresh1 = cv.threshold(gray, 254, 254, cv.THRESH_BINARY_INV)[1] #invert color to have white foreground for contour
thresh = cv.erode(thresh1, None, iterations=4)
thresh = cv.dilate(thresh, None, iterations=2)
# find contours in thresholded image, then grab the largest
# one

cnts, res = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv.contourArea) #find largest contour (shape of fish)
cnt = cv.drawContours(image, [c], -1, (0,255,0))  # Draw the largest contour in green

util.util.create_points(image=image, c=c)

# image = cv.putText(image,legend,(cx,cy), 1, 1, (255,0,0), 5)
#display the result image
cv.imshow("contours", image)
cv.waitKey()
cv.destroyAllWindows()