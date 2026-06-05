# 开发日志

## 第一天
- 环境配置：pip install opencv-python ultralytics torch torchvision
- TabError：混用Tab和空格，改用纯空格缩进
- 摄像头：电脑摄像头无法打开，改用手机DroidCam + WiFi连接

## 第二天
- 阅读代码，理解YOLO=大脑，OpenCV=眼睛
- 写README.md，录制演示视频，上传B站设为私密

## 第三天
- 性能调优：加FPS显示，基准帧率10-12帧
- 尝试降分辨率到320x240，帧率反降至9-10帧
- 分析瓶颈：WiFi传输限制，CPU做resize额外消耗
- 换用yolov5n模型，帧率跃升至20帧
- 结论：网络传输场景下，换轻量模型比砍分辨率更有效