''' Resize, Flipping, Cropping, Translation, Rotation '''

import cv2 as cv 
import numpy as np 

img = cv.imread(r"img2.png")

# Resize:
'''
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow("Image", resized)
'''

# Flipping 
'''
flipped = cv.flip(img, -1)  # NOTE: 1 -> Horizontal Flip 0 -> Vertical Flip -1 -> Both
cv.imshow("Original", img)
cv.imshow("Flipped_Image", flipped)
'''

# Cropping 
'''
crop = img[100:500 , 200:300]
cv.imshow("Cropped_Image", crop)
'''

# Translation
'''
def translate(img, x, y):
    trans_mat = np.float32([1, 0, x], [0, 1, y])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimension)
'''

# Rotation 

import cv2 as cv
import numpy as np 

img = cv.imread(r"images\csbldg.jpg")

def rotate(img, angle, rotpoint = None):
    (height, width) = img.shape[:2] # 0 -> height & 1 - > Widht
    
    if rotpoint is None:
        rotpoint = (width // 2, height // 2)
        
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimesions = (width, height)
    
    return cv.warpAffine(img, rotmat, dimesions)

rotated = rotate(img, 90)
cv.imshow("Original Image", img)
cv.imshow("Rotated Image", rotated)
cv.waitKey(0)


cv.waitKey(0)