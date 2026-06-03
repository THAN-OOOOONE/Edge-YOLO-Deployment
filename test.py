from ultralytics import YOLO
import cv2

model = YOLO("yolov5s.pt")
cap = cv2.VideoCapture("http://192.168.199.161:4747/video")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated = results[0].plot()
    cv2.imshow("AI检测", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()