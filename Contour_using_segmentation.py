
import cv2
import numpy as np

#Read the image
img = cv2.imread('two.tif')

#Convert the image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply thresholding on the grayscale image to obtain binary image
ret, thresh = cv2.threshold(gray,210,255,0)

#Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Find the contour with the maximum area
cnt = max(contours, key = lambda x: cv2.contourArea(x))

#Draw the contour on the original image
cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

#Show the image
cv2.imshow('Optic Disc Detection', img)

#Wait for a keypress
cv2.waitKey(0)

#Destroy all the windows
cv2.destroyAllWindows()