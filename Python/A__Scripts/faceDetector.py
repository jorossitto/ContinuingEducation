#Goal to Detect faces from a picture
import cv2
from C_Data.configs import *

#The Haar Classifiers
faceCascade = cv2.CascadeClassifier(configs.HAAR_FACE)
eyeCascade = cv2.CascadeClassifier(configs.HAAR_EYE)

img = cv2.imread(configs.MORE_PLAYERS)

faces = faceCascade.detectMultiScale(img, 1.2, 2)

print('Faces found: ', len(faces))
print('The image height, width, and channel: ', img.shape)
print('the coordinates of each face detected: ', faces)

#loop over the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    roiFace = img[y:y+h, x:x+w]
    eyes = eyeCascade.detectMultiScale(roiFace, 1.2, 3)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roiFace, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)

#show image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
