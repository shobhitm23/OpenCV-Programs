import cv2

image = cv2.imread("ShobhitMakhija_ResumePic.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Linkedin", image)
cv2.imshow("Filter 1", gray_image)
cs2.waitKey(0)
cv2.destroyAllWindows()
