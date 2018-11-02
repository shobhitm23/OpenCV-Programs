import cv2 as cv
import numpy as np
import matplotlib as plt

# load the image
im = cv.imread("Donuts.jpeg");

# load the image in grayscale
im2 = cv.imread("Donuts.jpeg", 0);

cv.imshow('image',im);
cv.imshow('grayscale',im2);

cv.waitKey(0);
cv.destroyAllWindows();
