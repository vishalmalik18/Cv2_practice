import numpy as np
import cv2

#live webcam sketch
def sketch(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    canny_edges=cv2.Canny(img_gray_blur,10,70)
    _,mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY)
    return mask

# cap=cv2.VideoCapture(0)
# while True:
#     ret,frame=cap.read()
#     cv2.imshow("Live sketch ",sketch(frame))
#     if cv2.waitKey(1)==13:
#         break
# cap.release()
# cv2.destroyAllWindows()

cap=cv2.VideoCapture(r"file_path")
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow("video sketch",sketch(frame))
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# 30 - fps
