import cv2
import numpy as np
def sub_b(image_path,lower_color,upper_color):
    image=cv2.imread(image_path)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    l_b=np.array(lower_color,dtype=np.uint8)
    u_p=np.array(upper_color,dtype=np.uint8)
    mask=cv2.inRange(hsv,l_b,u_p)
    mask_i=cv2.bitwise_not(mask)
    foreground=cv2.bitwise_and(image,image,mask=mask_i)
    cv2.imshow("original image",image)
    cv2.imshow("background subtracted image",foreground)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    image_path="sample.jpeg"
    lower_colour=[30,30,30]
    upper_color=[255,255,255]
    sub_b(image_path,lower_color,upper_color)
    