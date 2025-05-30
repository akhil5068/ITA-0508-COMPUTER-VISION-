import cv2
image = cv2.imread('sample.jpeg')
watermark_text = 'AKHIL'
position = (50, 50)  # (x, y)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 0)  # white
thickness = 2
watermarked_image = image.copy()
cv2.putText(watermarked_image, watermark_text, position, font, font_scale, color, thickness, cv2.LINE_AA)
cv2.imwrite('watermarked.jpg', watermarked_image)
