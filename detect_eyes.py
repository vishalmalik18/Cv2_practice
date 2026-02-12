eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


def detect_eyes(img):
    eye_img = img.copy()
    eye_rect = eye_cascade.detectMultiScale(eye_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in eye_rect:
        cv2.rectangle(eye_img,(x,y),(x+w,y+h),(225,225),10)
    return eye_img
