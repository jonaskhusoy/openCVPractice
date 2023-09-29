import cv2 as cv
import numpy as np

def create_points(image, c):
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
    
    return image
