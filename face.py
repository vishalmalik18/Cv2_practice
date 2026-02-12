face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img cv2.imread("your_image_path")

def adjust_face(img):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(225,225),10)
    return face_img
