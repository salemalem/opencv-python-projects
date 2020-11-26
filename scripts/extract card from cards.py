import cv2
import numpy as np

img = cv2.imread("../resources/cards.png")

# regular card size
width, height = 225, 350

# corners of card at "cards" image
"""
if you are trying your own image and want to know the coordinates
go to https://inkplant.com/tools/image-coordinates
hover over the position and it will show the x, y coordinates
"""
points1 = np.float32([[8, 265], [302, 80], [562, 492], [262, 683]])

# positioning them at new image
points2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

# transforming into matrix perspective
matrix = cv2.getPerspectiveTransform(points1, points2)
transformedImage = cv2.warpPerspective(img, matrix, (width, height))

# showing an image
cv2.imshow("Image", transformedImage)

# necessary to keep the window unclosed
cv2.waitKey(0)