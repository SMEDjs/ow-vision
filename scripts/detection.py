from typing import Counter
from mss import mss
import cv2
import numpy as np
import time
import pandas as pd
from ultralytics import YOLO
import pyautogui
import keyboard
import threading
import math

MONITOR_WIDTH = 1920
MONITOR_HEIGHT = 1080
MONITOR_SCALE = 5
region = (int(MONITOR_WIDTH/2-MONITOR_WIDTH/MONITOR_SCALE/2),int(MONITOR_HEIGHT/2-MONITOR_HEIGHT/MONITOR_SCALE/2),int(MONITOR_WIDTH/2+MONITOR_WIDTH/MONITOR_SCALE/2),int(MONITOR_HEIGHT/2+MONITOR_HEIGHT/MONITOR_SCALE/2))
x,y,width,height = region
screenshotCenter = [int((width-x)/2),int((height-y)/2)]

model = YOLO('best.pt')
model.to("cuda")
model.conf = 0.70
model.maxdet = 10
model.apm = True 

# TRIGGER bot
triggerbot = False
triggerbotToggle = [True]
lastClick = 0
cooldown = 0.2 # cooldown between click in seconds

with mss() as stc:
    while True:
        closest_part_distance = 100000
        closest_part = -1

        screenshot = np.array(stc.grab(region))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        currentTime = time.time()

        frame = model.predict(screenshot, save=False, classes=[1])
        boxes = frame[0].boxes.xyxy.cpu().numpy()
        positions_frame = pd.DataFrame(frame[0].cpu().numpy().boxes.data, columns = ['xmin', 'ymin', 'xmax', 'ymax', 'conf', 'class'])
        
        for i, row in enumerate(positions_frame.iterrows()):
            try:
                xmin, ymin, xmax, ymax, confidence, category = row[1].astype('int')
                centerX = (xmax-xmin)/2+xmin 
                centerY = (ymax-ymin)/2+ymin
                distance = math.dist([centerX,centerY],screenshotCenter)

                cv2.rectangle(screenshot,(xmin,ymin),(xmax,ymax), (255,0,0), 2)

                if int(distance) < closest_part_distance:
                    closest_part_distance = distance
                    closest_part = i
            except:
                print("",end="")

        if keyboard.is_pressed('²'):
            if triggerbotToggle[0] == True:
                triggerbot = not triggerbot
                triggerbotToggle[0] = False
                thread = threading.Thread(target=cooldown, args=(triggerbotToggle,0.2,))
                thread.start()

        if closest_part != -1:
            xmin = positions_frame.iloc[closest_part,0]
            ymin = positions_frame.iloc[closest_part,1]
            xmax = positions_frame.iloc[closest_part,2]
            ymax = positions_frame.iloc[closest_part,3]
            if currentTime - lastClick > cooldown and triggerbot == True and screenshotCenter[0] in range(int(xmin),int(xmax)) and screenshotCenter[1] in range(int(ymin),int(ymax)):
                print("click")
                pyautogui.click() 
                lastClick = currentTime

        cv2.rectangle(screenshot, (0, 0), (20, 20), (0, 255, 0) if triggerbot else (0, 0, 255), -1)
        cv2.imshow("frame",screenshot)
        if(cv2.waitKey(1) == ord('l')):
            cv2.destroyAllWindows()
            break