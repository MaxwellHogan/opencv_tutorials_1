'''
This is an easy warm up. The tasks the you need to do are:
    - import the required packages (in this case opencv)
    - read the image (the image's filename is "images/robot1.jpg")
    - display the image 
    - save the image 
    - call cv2.waitKey(0) - this keeps the program from closing.
    - call cv2.destroyAllWindows() - make sure the windows are not left open.
'''
### Import OpenCV #####
import cv2

#######################
### Read an Image #####
img = cv2.imread("images/robot1.jpg")


#########################
### Display the image ###
cv2.imshow('img', img)

###########################
##### Saving Image ########


########################
#### Call waitKey ######


########################
##Exiting Function######