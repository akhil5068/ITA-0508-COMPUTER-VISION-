import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread('sample.jpeg', 0)

# Apply thresholding to get binary image
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(binary, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original', binary)
cv2.imshow('Eroded', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
