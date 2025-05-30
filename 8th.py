import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('sample.jpeg')  # Replace with your image file path

# Step 2: Convert image to grayscale (optional but recommended for morphology)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)

# Step 4: Apply dilation
dilated_image = cv2.dilate(gray, kernel, iterations=1)

# Step 5: Show the original and dilated images
cv2.imshow('Original Image', gray)
cv2.imshow('Dilated Image', dilated_image)

# Wait for a key and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
