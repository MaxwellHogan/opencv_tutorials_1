'''
In this script we are going to apply two very common morphological 
operators: Erosion and Dilation. 
'''
### Import OpenCV & numpy #####
import cv2
import numpy as np


#######################
### Read an Image #####

img = cv2.imread('WesternBlot2.jpg')

#########################
#### Create a Kernel ####

########################
###### Erode Image ##### 


######################
###### Dilate ########


### Display the results ###

cv2.imshow('Main', img)
cv2.waitKey(0)

cv2.imshow('Erroded', )
cv2.waitKey(0)

cv2.imshow('Dilate', )
cv2.waitKey(0)

########################


##Exiting Function######

cv2.destroyAllWindows()

########################