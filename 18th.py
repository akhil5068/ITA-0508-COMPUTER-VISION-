import cv2

# Load the image
image = cv2.imread('sample.jpeg')

# Define the ROI (y1:y2, x1:x2)
roi = image[50:150, 100:200]  # adjust as needed

# Paste the ROI to a new location (e.g., top-left corner)
image[0:100, 0:100] = roi
cv2.imwrite('modified.jpg', image)

