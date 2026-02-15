import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow # for googl colab

img = cv2.imread('your_image')

resized_image = cv2.resize(img,(400,300))

# for gaussian
cv2_imshow(cv2.GaussianBlur(resized_image,(5,5),0))

# for median
cv2_imshow(cv2.medianBlur(resized_image,11))

#f for bilateralFilter
cv2_imshow(cv2.bilateralFilter(resized_image,15,150,150)
           
