import cv2
import numpy as np

# Read image
img = cv2.imread("two.tif", 0)
# Apply dilation and erosion to remove some noise
kernel = np.ones((3,3),np.uint8)
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 2)
# Apply threshold to get image with only black and white
ret, thresh = cv2.threshold(img_opening,210,255,cv2.THRESH_BINARY)
# Find contours of the filtered image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Find the contour of largest area and draw it
cnt = max(contours, key = lambda x: cv2.contourArea(x))
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# Show resultant image
cv2.imshow("Image", img)
cv2.waitKey(0)