'''
This script will be more easy going than the last one. 
We will be resizing an image. I have filled in some code below,
it is up to you to fill in the gaps. The tasks are as followed:
    - get and store the dimensions of the image.
    - compute the new dimensions if we are going to scale the image by 1/2
    - use these new dimensions to resize the image.
    - display the new image.

hint: https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d

'''

### Import OpenCV  #####
import cv2

#######################
### Read an Image #####
img = cv2.imread('images/robot2.jpg')

#####################################
#### Get the Dimension of Image #####
h, w, c = 

print(w, h, c)

#########################
###### Scaling ##########
w = int(w
h = int(h

########################
##### Resize ###########


#########################
### Display the image ###

cv2.imshow('Main Image', img)
cv2.waitKey(0)

cv2.imshow('resized', )
cv2.waitKey(0)

########################
##Exiting Function######

cv2.destroyAllWindows()

########################