'''
In this script we are going to apply two very common morphological 
operators: Erosion and Dilation. Both operations involve convolving an
image with some kernal, so the first task is to define the kernel that
will be scanned  across an image. It is a good idea to define use a 
variable to set the size so that it can be adjusted later. The remainder 
tasks are outlined below. 

In erosion, the kernel is scanned over the image, we compute the maximal
pixel value overlapped by the kernel and replace the pixel in the centre
of the kernel with that maximal value. 

In dilation, the kernel is scanned over the image, we compute the minimal
pixel value overlapped by the kernel and replace the pixel in the centre
of the kernel with that minimal value. 

hint: https://docs.opencv.org/4.x/db/df6/tutorial_erosion_dilatation.html

'''
### Import OpenCV & numpy #####
import cv2
import numpy as np


#######################
### Read an Image #####

img = cv2.imread('images/city_binary.png')

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