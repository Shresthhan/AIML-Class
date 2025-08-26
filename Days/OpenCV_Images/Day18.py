import cv2 as cv

# Loading and Displaying the Image
img = cv.imread(r"img1.jpg")
resize = cv.resize(img , (700,500))

cv.imshow("Image", resize)

# Average Blurring NOTE: Avg blurring le Intensity hercha 
'''
avg_blur = cv.blur(resize, (5,5))
cv.imshow("Avg_Blur", avg_blur)
'''
# Median Bluring NOTE: Esle ni Intensity nai hercha plus outliers le affect na garne bhako le more preferable 
'''
md_blur = cv.medianBlur(resize, 3) # -> (3,3)
cv.imshow("Median_Blur", md_blur)
'''

# Gaussian Blur NOTE -> Weight ko aadhar ma kaam garcha 
'''
Gauss_Blur = cv.GaussianBlur(resize, (5,5), 0)  0 -> sigmaX oripari ko pixels le ni effect garne outside window plus sigmaX ma horizontal pixels matra hercha i.e. X-axis 
cv.imshow("Gaussian_Blur", Gauss_Blur)
'''

# BiLateral Blur NOTE -> Weighnt nai hercha plus edges ni consider garcha (Intelligent Algorithm) ra esma sigmaS(space) le both horizontal ra vertical hercha i.e. both x and y axis window bahira ko pixel le window bhitra ko pixel lai kati effect garcha 
# Plus sigmaC(colour) ni huncha window bahira ko pixel ko colour le window bhitra ko pixel ma parne effect 
bilat_Blur = cv.bilateralFilter(resize, 15, 20, 20) #(img, window, SigmaC, SigmaS)
cv.imshow("Bilateral_Blur", bilat_Blur)

cv.waitKey(0)


# Resource kam cha vane use Average and Median 
# Resource dher cha ra vane Gaussian ra Bilateral 
# Accuracy chahincha vane Bilateral 
# Generally (5,5) ko window bata start huncha 
