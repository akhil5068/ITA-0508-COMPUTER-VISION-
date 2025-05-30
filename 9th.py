import cv2
image = cv2.imread('sample.jpeg')  
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image (2x)', bigger)
cv2.imshow('Smaller Image (0.5x)', smaller)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
