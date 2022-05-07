import cv2
import numpy as np

img = cv2.imread( 'two.tif' )

# convert the input image to LAB color space
lab = cv2.cvtColor( img , cv2.COLOR_BGR2LAB )

# split the image into L, A and B channels
l , a , b = cv2.split( lab )

# apply CLAHE to L channel
clahe = cv2.createCLAHE( clipLimit=3.0 , tileGridSize=(8 , 8) )
cl = clahe.apply( l )

# merge the CLAHE enhanced L channel with the original A and B channels
limg = cv2.merge( (cl , a , b) )

# convert the LAB image back to RGB color space
final = cv2.cvtColor( limg , cv2.COLOR_LAB2BGR )

# display the output image
cv2.imshow( 'Enhanced Image' , final )
cv2.imshow( 'Original Image' , img )
cv2.waitKey( 0 )