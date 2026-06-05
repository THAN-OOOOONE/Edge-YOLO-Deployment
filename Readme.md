# YOLOv5实时目标检测

## 项目简介
在Windows上部署YOLOv5模型，利用手机摄像头实现实时目标检测。
本项目是我“边缘AI部署”学习路线的第一个里程碑。

## 技术栈
- Python 3.10
- OpenCV (计算机视觉库)
- Ultralytics YOLOv5 (目标检测模型)
- PyTorch (深度学习框架)

## 运行环境
- Windows 10/11
- Python 3.10
- 所需库："opencv-python", "ultralytics", "torch"
- 可选：Android/iOS手机 + DroidCam/EpocCam App

## 如何使用
1.  克隆本仓库到本地
2.  安装依赖："pip install opencv-python ultralytics torch torchvision"
3.  准备摄像头：
    -   使用电脑自带摄像头：代码中"cv2.VideoCapture(0)"
    -   使用手机摄像头：下载DroidCam，记录App显示的IP地址，修改代码
4.  运行：`python test1.py`
5.  按 `q` 键退出程序

## 效果演示
[点击查看演示视频]（https://www.bilibili.com/video/BV1PFEP6vEx1/?vd_source=78ae6d79cdbfd741a8001641afdd6589）

- 实时检测画面中的物体（人、书本、杯子等）
- YOLOv5s模型，在CPU上运行

## 踩坑记录
- **TabError**: 复制代码导致缩进混乱，需统一使用空格或Tab键
- **摄像头打不开**: Windows隐私权限设置，或使用手机替代方案
- **Git推送冲突**: 本地和远程文件重名，使用"git pull"解决
- **TabError**: 复制代码导致缩进混乱，需统一使用空格或Tab
- **摄像头打不开**: Windows隐私权限，或改用手机DroidCam替代
- **WiFi传输瓶颈**: 优化分辨率后FPS反降，定位原因为WiFi传输成为瓶颈，非本地算力问题
- **模型选型**: yolov5s(12帧) → yolov5n(20帧)，轻量模型显著提升端侧性能

## 作者
- 民办二本，Gap期自学边缘AI部署
- 目标岗位：边缘AI应用开发 / AI模型部署工程师
- 学习记录：持续更新中...

