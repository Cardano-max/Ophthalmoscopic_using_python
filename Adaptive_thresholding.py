import cv2
import numpy as np

# Read the image
img = cv2.imread('two.tif', 0)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the index of the largest contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt = contours[max_index]

# Draw the contour with the maximum area
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

# Show the image
cv2.imshow('Image', img)
cv2.waitKey(0)