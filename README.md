# ow-vision

## About
ow-vision is an **AI** to detect enemy on **Overwatch 2** ! It can detect hero and their head

**Features:**

* ✅ Detect enemy and enemy's head
* ✅ Detect any hero
* ✅ Trigger bot to click automatically on enemy head

Made with **passion**, **raggae** and **YOLOv8** 

<a href="https://ultralytics.com/yolov8" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png">
</a>

## Content

The training
![training](https://cdn.discordapp.com/attachments/941415112135307314/1097664342272520254/image.png)

## Trigger bot
ow-vision has a script to click automatically on enemy head *(not allowed by Overwatch 2)*

Example:
![trigger bot](https://cdn.discordapp.com/attachments/941415112135307314/1097663491814465566/ApplicationFrameHost_jwhkqyaIr9.gif)
## Code
### run 
```py
python /scripts/detection.py
```
### train
```py
!yolo train model=yolov8n.pt data=./datasets/v2/data.yaml epochs=150 imgsz=736 project=/models/result/v2 device=0
```

## Changelogs

### Version 2
Recoded the AI and added a larger dataset

### Version 1.1
Started hero detection
![hero detection](https://cdn.discordapp.com/attachments/941415112135307314/1097661599495504023/image.png)

### Version 1 (test)
The AI could detect bot in the training range

![bot detection](https://cdn.discordapp.com/attachments/1095042451607134259/1097660539741675643/image.png)