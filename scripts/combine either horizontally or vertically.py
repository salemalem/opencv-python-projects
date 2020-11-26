import cv2
import numpy as np

img = cv2.imread("../resources/small-sunflowers.jpg")

# horizontally combined images
imgHor = np.hstack((img, img))
# vertically combined images
imgVer = np.vstack((img, img))

cv2.imshow("Horizantally combined images", imgHor)
cv2.imshow("Vertically combined images", imgVer)

# necessary to keep the window unclosed
cv2.waitKey(0) # put milliseconds as an argument 0 means infinite