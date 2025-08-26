'''
Edge -> The line/ curve showing the change in gradient between two pixels or sections of image. i.e 
        Duita intensity bhako pixels chutaune line. Edge le change hercha 

Conture -> The line or curve  joining the pixels having same intensity or colour. Conture le similarity hercha
'''

import cv2 as cv 

img = cv.imread(r"red.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred_img = cv.GaussianBlur(gray, (1, 1), 0)

# Canny 
edges = cv.Canny(blurred_img, 100, 200)
contures_canny, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 

count1 = len(contures_canny)

# Threshold 
thres_val, thres_img = cv.threshold(blurred_img, 150, 255, cv.THRESH_BINARY)
conture_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(conture_thres)

print(count1)
print(count2)

# Draw the COntures 
img_thres = img.copy()
img_canny = img.copy()

cv.drawContours(img_canny, contures_canny, -1, (0, 255, 0), 2)
cv.drawContours(img_thres, conture_thres, -1, (0, 0, 255), 2)

cv.imshow("Contour_Canny", img_canny)
cv.imshow("Contour_Thres", img_thres)

cv.waitKey(0)
cv.destroyAllWindows()