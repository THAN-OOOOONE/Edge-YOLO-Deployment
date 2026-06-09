#从ultralyatics库中导入YOLO类
from ultralytics import YOLO
#导入OPENCV库
import cv2
import time

#创建一个YOLO模型对象，yolov5s.pt是引用的功能文件，从网上下载
model = YOLO("yolov5n.pt")
#打开摄像头，调用的是手机DroidCam的IP地址
cap = cv2.VideoCapture("http://192.168.199.161:4747/video")
#记录第一针开始前的时间
prev_time = time.time()

#循环判断
while True:
	#从摄像头读取一帧画面，用ret值判断是否读取到，frame表示图像数据
    ret, frame = cap.read()
    frame = cv2.resize(frame,(320,240))
#如果没有读取到ret值，说明摄像头断连，终止循环
    if not ret:
        break
#把画面frame传输到模型做推理,aresults会保存获得的信息
    results = model(frame)
#用plot函数把检测出来的值在原始画面上标出来
    annotated = results[0].plot()
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
#在画面上显示PFS
    cv2.putText(annotated,f"FPS:{int(fps)}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
#用窗口显示检测出来的值，窗口命名为AI检测
    cv2.imshow("AI检测", annotated)
#用waitKey让画面停留1毫秒，然后判断是否点击Q键，是就退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#终止循环并释放摄像头资源
cap.release()
#关闭所有Opencv的窗口
cv2.destroyAllWindows()


