import cv2
import numpy as np

img = cv2.imread('two.tif')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
eq = cv2.equalizeHist(gray)

# Stack the images to get out output
res = np.hstack((gray,eq)) #stacking images side-by-side

# Save image
# cv2.imshow(,res)
cv2.imshow('res.png',res)
#Wait for a keypress
cv2.waitKey(0)

#Destroy all the windows
cv2.destroyAllWindows()

