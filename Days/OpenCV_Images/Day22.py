'''  THRESHOLD  '''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r"img2.png")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Simple Threshold 
'''
threshold , thres_Img = cv.threshold(gray, 135, 255, cv.THRESH_BINARY)
threshold , thres_Img_INV = cv.threshold(gray, 135, 255, cv.THRESH_BINARY_INV)# INV le thres vanda besi lai black banaucha i.e. ulto kaam garcha 
cv.imshow("Simple Threshold Image", thres_Img)
cv.imshow("Simple Threshold Image INV", thres_Img_INV)
'''

# Adaptive Threshold -> Aaghi hamile aafai threshold 135 rakheko thim tara esma chai aafai calculate garcha for a particular frame 
'''
adp_thres_Img_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
adp_thres_Img_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5) #Kernel size 5-15 maxly
cv.imshow("Adaptive Mean", adp_thres_Img_mean)
cv.imshow("Adaptive Gaussian", adp_thres_Img_gaussian)

# NOTE: Gaussian accurate bhaye ni computation herera max mean nai use huncha
'''

# Colour Spaces
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# cv.imshow("HSV", hsv)
# cv.imshow("HLS", hls)
# cv.imshow("YCrCb", ycrcb)
cv.imshow("RGB", rgb)
# cv.imshow("LAB", lab)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)

'''
NOTE: Face Detection -> Gray -> HSV -> YCrCb 
NOTE: Colour Segmentation -> HSV
NOTE: Thresholding -> Gray 
NOTE: Object Tracking -> HSV -> LAB
NOTE: Image/ Video COmpression -> YCrCb
NOTE: Image Enhancement -> LAB 
'''