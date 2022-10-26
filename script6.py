'''
In this script we are going to continue the theme of investigating 
opencv's built in functions. Specifically we are going to look at 
the bluring operations availiable.

These include:
    - Gaussian Blur
    - Median Blur

If you have reached this point by yourself, I suggest looking into 
the hint for how to use these functions. On of these functions will 
be important in the final exercise so I suggest reading the details.

hint: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
'''
#############################
### Import OpenCV & numpy ###
import cv2
import numpy as np


#######################
### Read an Image #####
img = cv2.imread('images/robot2.jpg')

####################################
######### Gaussian Blur ############


####################################
########## Median Blur###############

###########################
### Display the results ###

cv2.imshow('Main', img)
cv2.waitKey(0)

cv2.imshow('Gaussian', )
cv2.waitKey(0)

cv2.imshow('Median', )
cv2.waitKey(0)

########################
##Exiting Function######

cv2.destroyAllWindows()

########################