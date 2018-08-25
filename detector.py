import numpy as np
import cv2

tem_photo = 'example.tif'

image_original = cv2.imread(tem_photo)
image_resized = cv2.resize(image_original, (1000, 1000))
image_blurred = cv2.GaussianBlur(image_resized, (3,3),0)
output = image_resized.copy()
gray = cv2.cvtColor(image_blurred, cv2.COLOR_BGR2GRAY)

def find_circles(gray): #, min_dist, min_r, max_r, dp=1, param1=200, param2=20):
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 19, 
                               param1 = 200, param2 =21, minRadius = 20, 
                               maxRadius = 60)
	if circles is not None:
		circles = np.round(circles[0, :], decimals=1)
		for (x, y, r) in circles:
			cv2.circle(output, (x, y), r, (0, 255, 0), 1)

find_circles(gray)

cv2.imshow("output", np.hstack([image_resized, output]))
cv2.waitKey(0)