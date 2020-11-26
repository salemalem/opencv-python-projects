import cv2
import numpy as np

img = cv2.imread("../resources/black-friday.jpg")

# Resizing image (Making it smaller) because original image is too big
scale_percent = 5
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dimensions = (width, height)

resizedSmallerImage = cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)

# Showing an image
cv2.imshow("Resized Smaller Image", resizedSmallerImage)

# necessary to keep the window unclosed
cv2.waitKey(0)  # put milliseconds as an argument 0 means infinite
