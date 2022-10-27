'''
This is where stuff will start to get tricky! We are going to do some operations between images.
These operations are not themselves challenging. However, as you learned in class,
each pixel in an image can be a value between 0 and 255. Hence, there is risk that 
by summing or subtracting we may create a new image outside this range. 

You will see in this notepad I have provided some code to get you started.

The tasks are outlined below.

'''
### Import OpenCV & numpy #####
import cv2
import numpy as np

#######################
### Read an Image #####

img1 = cv2.imread('images/wb1.jpg')
img2 = cv2.imread('images/wb2.jpg')

##########################################################
### Convert the images to float for further operations ###
### hint: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html

img1 = 
img2 = 

#####################
#### Add Images #####
img_add = 


###################################
##### Subtract img1 from img2 #####
img_subtract = 


###########################
##### Multiply Images #####
img_multiply = 

####################################################
##### Normalise the new images between 0 - 255 #####
## hint: https://stats.stackexchange.com/questions/70801/how-to-normalize-data-to-0-1-range


#############################################
#### convert all images back to np.uint8 ####


#########################
### Display the results ###

cv2.imshow('Image 1', )
cv2.waitKey(0)

cv2.imshow('Image 2', )
cv2.waitKey(0)

cv2.imshow('Added', )
cv2.waitKey(0)

cv2.imshow('Subtract', )
cv2.waitKey(0)

cv2.imshow('Multiply', )
cv2.waitKey(0)

########################
##Exiting Function######
cv2.destroyAllWindows()

########################