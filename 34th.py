import numpy as np
import cv2
def create_circle_image(image_size):
 height, width = image_size # Extract height and width
 image = np.ones((height, width, 3), dtype=np.uint8) * 255
 center = (width // 2, height // 2) # Center of the image
 radius = min(width, height) // 4 # Radius is 1/4th of the smallest dimension
 cv2.circle(image, center, radius, (0, 0, 255), 2)
 cv2.imshow("Circle Image", image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))
create_circle_image((user_height, user_width))