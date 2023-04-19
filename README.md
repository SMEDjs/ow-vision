# ow-vision

## About
ow-vision is an **AI** to detect enemy on **Overwatch 2** ! It can detect hero and their head and click automatically on it 

![triggerbot](https://cdn.discordapp.com/attachments/949825336961564672/1098224993885765662/triggerbot.gif)

**Features:**

* ✅ Detect enemy and enemy's head
* ✅ Detect any hero
* ✅ Trigger bot - click automatically on enemy head
* ✅ Fast - 20ms to detect and click

Made with **passion**, **raggae** and **YOLOv8** 

<a href="https://ultralytics.com/yolov8" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png">
</a>

## Content

The training
![training](https://cdn.discordapp.com/attachments/941415112135307314/1097664342272520254/image.png)
![hero](https://media.discordapp.net/attachments/949825336961564672/1097695463836229662/image.png?width=677&height=675)

## Trigger bot
ow-vision has a script to click automatically on enemy head *(not allowed by Overwatch 2 so use at your own risk)*

Example in game:
![trigger bot](https://cdn.discordapp.com/attachments/941415112135307314/1097663491814465566/ApplicationFrameHost_jwhkqyaIr9.gif)
*https://cdn.discordapp.com/attachments/941415112135307314/1097663491814465566/ApplicationFrameHost_jwhkqyaIr9.gif*
## Code
### run 
```py
python /scripts/main.py
```
### train
```py
!yolo train model=yolov8n.pt data=./datasets/v2/data.yaml epochs=150 imgsz=736 project=/models/result/v2 device=0
```

### settings
```py
# Detection.py
settings = {"toggleKey": "²", # the key to toggle the trigger bot, the square on the frame represent the state (red=disabled)
            "cooldown": 1.1, # cooldown between clicks in seconds (only for mode 0)
            "detect": [1], # detect enemy [0] or enemyHead [1] and [0, 1] for both
            "triggerDelay": 0} # delay between clicking on the target in seconds, 0 is fine
```

## Changelogs

### Version 2
Recode and larger dataset
![hero](https://media.discordapp.net/attachments/949825336961564672/1097695463836229662/image.png?width=677&height=675)
### Version 1.1
Started hero detection
![hero detection](https://cdn.discordapp.com/attachments/941415112135307314/1097661599495504023/image.png)

### Version 1 (test)
The AI could detect bot in the training range

![bot detection](https://cdn.discordapp.com/attachments/1095042451607134259/1097660539741675643/image.png)