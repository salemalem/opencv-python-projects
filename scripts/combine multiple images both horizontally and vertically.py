# this script is more advanced than "combine either horizontally or vertically"
import cv2
import numpy as np

# taken from https://www.murtazahassan.com/courses/learn-opencv-in-3-hours/lesson/chapter-6-joining-images/
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


# reading an image
img = cv2.imread("../resources/small-cat.png")

# 1st argument is scaling: we are scaling down by putting 0.5
# 2nd arg is matrices (plural of matrix)
stackedImage = stackImages(0.5, ([img, img, img]))
"""
you can also put stackImages(0.5, ([img, img, img], [img, img, img]))
to create 2 rows of 3 column image instead of current 1 row
"""

# showing an image
cv2.imshow("Stacked Image", stackedImage)

# necessary to keep the window unclosed
cv2.waitKey(0) # put milliseconds as an argument 0 means infinite