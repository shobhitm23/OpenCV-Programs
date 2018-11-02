import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('C:\\Python Programs\\haarcascade_frontalface_alt2.xml');
eye_cacade = cv.CascadeClassifier('C:\\Python Programs\\haarcascade_eye.xml');

img = cv.imread('ShobhitMakhija_ResumePic.jpeg');
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY);

faces = face_cascade.detectMultiScale(gray,1.3,5);

for(x,y,w,h) in faces:
    img = cv.rectangle(img,(c,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w];
    roi_color = img[y:y+h, x:x+w];
    eyes = eye_cascade.detectMultiScale(roi_gray);
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey,ex+eh), (0,255,0),2);

cv.imshow('img',img);
k = cv.waitKey(0);
if k == 27:         # ESC to exit
    cv.destroyAllWindows();
elif k == ord('s'): # wait for 's' key to be clicked
    cv.destroyAllWindows();
