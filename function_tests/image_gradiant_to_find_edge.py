import cv2 as cv
import numpy as np

path = "C:\OpenCV\images\klippfisk_demo.jpg" #img path

img = cv.imread(path) #cv img object
result = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

result = cv.Laplacian(result, cv.CV_64F)


cv.imshow("original",img)
cv.imshow("result", result)
cv.waitKey()
cv.destroyAllWindows