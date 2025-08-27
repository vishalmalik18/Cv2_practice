face_identifier=cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_identifier=cv2.CascadeClassifier(r"haarcascade_eye.xml")
cap=cv2.VideoCapture(r"file_path")

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_identifier.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        face_gray=gray[y:y+h,x:x+w]
        face_color=frame[y:y+h,x:x+w]
        eyes=eye_identifier.detectMultiScale(face_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("Real Time face and eye detection",frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destraoyAllWindows()
