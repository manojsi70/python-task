import numpy as np
import cv2

height, width = 400, 400
gradient_image = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        gradient_image[y, x] = (255, 255 - int(255 * y / height), 255)

# Draw some shapes on the image
cv2.rectangle(gradient_image, (50, 50), (200, 200), (0, 255, 0), -1)  
cv2.circle(gradient_image, (300, 300), 50, (0, 0, 255), -1)  
cv2.line(gradient_image, (100, 100), (300, 300), (255, 0, 0), 3)  

# Display the custom image
cv2.imshow('Custom Image', gradient_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
