# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2

# read image as grey scale
img=cv2.imread('example_01.png')
# get image height, width

(h,w)= img.shape[:2]
# calculate the center of the image
center= (w/2, h/2)
angle90 = 90
scale=1.0



# Perform the counter clockwise rotation holding at the center
# 90 degrees
M=cv2.getRotationMatrix2D(center,angle90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))


cv2.imshow('Original Image',img)
cv2.waitKey(0)# waits until a key is pressed
cv2.destroyAllWindows()# destroys the window showing image

cv2.imshow('Image rotated by 90 degrees',rotated90)
cv2.waitKey(0)# waits until a key is pressed
cv2.destroyAllWindows()# destroys the window showing image

