import cv2 as cv 

# Reading Images
#img = cv.imread(r"img1.jpg")
#cv.imshow("Image", img)

# Resizing 
#resized = cv.resize(img, (500,500))
#cv.imshow("Image", resized)

# FLip Image 
'''
img = cv.imread(r"img2.png")
resized = cv.resize(img, (500,500))
flipped = cv.flip(resized, -1)
cv.imshow("Image", flipped)
cv.waitKey(0)
'''

# Converting to Grey Scale 
'''
img = cv.imread(r"img2.png")
resized = cv.resize(img, (500,500))

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Gray_Image", gray)
cv.waitKey(0)
'''

# Rectangle
'''
img = cv.imread(r"img2.png")
cv.rectangle(img, (50,50), (250,300), (0,255,0), 2)

cv.imshow("Rect_Image", img)
cv.waitKey(0)
'''

# Edge Detection 
## Canny -> ML model - pre-trained 
img = cv.imread(r"img4.jpg")
resized = cv.resize(img, (500,500))
edges = cv.Canny(resized, threshold1= 100, threshold2= 200)
cv.imshow("Edges", edges)
cv.waitKey(0)
























