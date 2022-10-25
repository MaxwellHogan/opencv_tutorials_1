'''
Next week we will be undertaking more complex operations, the first of
which is edge detection. You can look at the hint to get a better 
understanding of these operations. 

If you have made it to this point we have reached the end of the
material for this week, if we have reached the last 15 minutes of the
lab you may leave, alternatively, you may look to the hint for
information on using the canny edge detection. 

hint: https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
'''
#############################
### Import OpenCV & numpy ###
import cv2
import numpy as np


#######################
### Read an Image #####
img = cv2.imread('images/robot2.jpg')


#####################################
######### Edge Detection ############


###########################
### Display the results ###

cv2.imshow('main', img)
cv2.waitKey(0)


cv2.imshow('edges', )
cv2.waitKey(0)

########################
### Exiting Function ###

cv2.destroyAllWindows()
