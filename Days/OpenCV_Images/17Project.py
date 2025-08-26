import cv2 as cv

# Read Image 
img = cv.imread(r"img1.jpg")
resized = cv.resize(img, (500,500))

gray = cv.cvtColor(resized , cv.COLOR_BGR2GRAY) 

# Haar Cascade

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1 , minNeighbors = 3)

for (x, y, w, h) in faces:
    cv.rectangle(resized, (x,y), (x+w, y+h), (0,255,0), 2)
    
cv.imshow("Faces", resized)
cv.waitKey(0)

 