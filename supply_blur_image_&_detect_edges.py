import cv2
from google.colab.patches import cv2_imshow # for google colab
import numpy as np

img = cv2.imread('your_image')

resized_image = cv2.resize(img,(400,300))
blur_image = cv2.GaussianBlur(resized_img,(5,5),0)

# for canny 

cv2_imshow(cv2.Canny(gb_image,50,100))

# for sobel 

gray_img = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)

# Calculate Sobel derivatives
sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=5)

# Combine the two gradients
sobel_combined = cv2.sqrt(cv2.addWeighted(cv2.pow(sobelx, 2.0), 1.0, cv2.pow(sobely, 2.0), 1.0, 0.0))

cv2_imshow(np.uint8(sobel_combined))

# for prewitt

gray_img = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Define Prewitt kernels
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

# Apply kernels
prewitt_x = cv2.filter2D(gray_img_original, -1, kernelx)
prewitt_y = cv2.filter2D(gray_img_original, -1, kernely)

# Combine results
prewitt_combined = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

cv2_imshow(prewitt_combined)


