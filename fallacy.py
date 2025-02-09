import cv2
from ultralytics import YOLO

model = YOLO("./best.pt")
cam = "http://192.168.7.178:8080/video" #IP webcam link
cap = cv2.VideoCapture(0)
cap.open(cam)
print("check ===>", cap.isOpened())

while cap.isOpened():
    success, frame = cap.read()

    if success:
        frame = cv2.resize(frame, (700, 700))
        results = model(frame)
        for det in results:
            cls = det
            print(cls)
        cv2.imshow("WebCam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()