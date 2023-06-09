import cv2

smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_smile(gray,frame):
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        smiles=smile_cascade.detectMultiScale(roi_gray,1.7,22)
        for(ex,ey,ew,eh) in smiles:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,255),2)
    return frame

video_capture=cv2.VideoCapture(0)
while True:
    _,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect_smile(gray,frame)
    cv2.imshow("Video",canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 
video_capture.release()
cv2.destroyAllWindows()
