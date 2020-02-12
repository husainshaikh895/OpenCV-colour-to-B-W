__author__ = 'Husain Shaikh'

# Converting a Coloured image to Black and white one

#  we first need to convert it to Grayscale then to B&W
# Grayscale will remove the colours but it will preserve shadows and light conditions
# Converting a Grayscale image to BW is easy but we can't do the same thing with coloured one
#  because there is no function to convert a colour image to black and white one
#  Hence we apply a threshold 
#  BW image will remove most of the details as only 2 colours are there ( 2 shades )
#  while in Grayscale there are 256 shades of each of the colours (black and white)

#  we'll use openCV for image manipulation
import cv2


# Store the original image
originalImage = cv2.imread('./miyoshi.jpg')
# convert it to grayscale so that only light conditions and shadows are prevserved without any colour
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# if the threshold is 150 or above then convert it to 255 else 0 for each pixle
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 150, 255, cv2.THRESH_BINARY)



# show the images and their transition when any key is pressed


# original
cv2.imshow('Original Image', originalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gray Scaled 
cv2.imshow('Gray Scaled image', grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Black and White
cv2.imshow('Black and white image', blackAndWhiteImage)
cv2.waitKey(0)
cv2.destroyAllWindows()



# save the images
cv2.imwrite('./miyoshi_g.jpg',grayImage)
cv2.imwrite('./miyoshi_bw.jpg', blackAndWhiteImage)
