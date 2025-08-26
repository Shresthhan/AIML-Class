'''   BITWISE OPERATIONS AND MASKING IN OPENCV   '''

import cv2 as cv
import numpy as np

'''
# Create two blank images 
img1 = np.zeros((300,300), dtype = "uint8")  # -> Blank image 300 by 300 diemntion with zero intensity 
img2 = np.zeros((300,300), dtype = "uint8")

# Draw a rectangle on img1 
cv.rectangle(img1, (50, 50), (250, 250), 255, -1)

# Draw a white circle on img2 
cv.circle(img2, (150, 150), 120, 255, -1) # -> Here -1 represents fill circle 

cv.imshow("Rectangle", img1)
cv.imshow("Circle", img2)

# And Operation
bit_and = cv.bitwise_and(img1, img2)
cv.imshow("AND", bit_and)

# OR Operation
bit_or = cv.bitwise_or(img1, img2)
cv.imshow("OR", bit_or)

# XOR Operation 
bit_xor = cv.bitwise_xor(img1, img2)
cv.imshow("XOR", bit_xor)

# NOT Operation 
bit_NOT1 = cv.bitwise_not(img1)
cv.imshow("NOT_Rec", bit_NOT1)

bit_NOT2 = cv.bitwise_not(img2)
cv.imshow("NOT_Cir", bit_NOT2)
'''

# Masking 
'''
img = cv.imread(r"img2.png")

# Create a mask 
img_mask = np.zeros(img.shape[:2], dtype = "uint8")

# Create a white circle in the mask
cv.circle(img_mask, (150, 150), 75, 255, -1)

# Apply the mask 
masked_img = cv.bitwise_and(img, img, mask = img_mask)

cv.imshow("Original", img)
cv.imshow("Mask", img_mask)
cv.imshow("Masked_Image", masked_img)
'''

img = cv.imread(r"img2.png")

# Splitting the Channels
B, G, R = cv.split(img)

# cv.imshow("Original", img)
# cv.imshow("Blue", B)
# cv.imshow("Green", G)
# cv.imshow("Red", R)

# merged = cv.merge([B, G, R])
# cv.imshow("Merged_Image", merged)

# zeros = np.zeros_like(B)
# blue_Visual = cv.merge([B, zeros, zeros])
# green_Visual = cv.merge([zeros, G, zeros])
# red_Visual = cv.merge([zeros, zeros, R])


# cv.imshow("Blue_Gray", blue_Visual)
# cv.imshow("Green_Gray", green_Visual)
# cv.imshow("Red_Gray", red_Visual)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
Blue_visual = cv.merge([B, img_gray, img_gray])
cv.imshow("Red", Blue_visual)

cv.waitKey(0)
cv.destroyAllWindows()
