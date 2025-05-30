import cv2
import numpy as np
image = cv2.imread('sample.jpeg', 0)
kernel = np.ones((15, 15), np.uint8)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Result", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
