import cv2 as cv
import numpy as np

path = "C:\OpenCV\images\klippfisk_demo.jpg" #img path

img = cv.imread(path) #cv img object
result = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(result, 250, 255, cv.THRESH_BINARY)

result = cv.Canny(mask, 100, 200)
cv.imshow("outline",result)
cv.waitKey()
cv.destroyAllWindows