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
from speedster import optimize_model
import torch


class Detection:
    def __init__(self):
        MONITOR_WIDTH = 1920
        MONITOR_HEIGHT = 1080
        MONITOR_SCALE = 5
        region = (int(MONITOR_WIDTH/2-MONITOR_WIDTH/MONITOR_SCALE/2),
                       int(MONITOR_HEIGHT/2-MONITOR_HEIGHT/MONITOR_SCALE/2),
                       int(MONITOR_WIDTH/2+MONITOR_WIDTH/MONITOR_SCALE/2),
                       int(MONITOR_HEIGHT/2+MONITOR_HEIGHT/MONITOR_SCALE/2))
        x, y, width, height = region
        screenshotCenter = [int((width-x)/2), int((height-y)/2)]
        model = YOLO('../models/v2.pt')
        model.to("cuda")
        model.conf = 0.70
        model.maxdet = 10
        model.apm = True
        triggerbot = False
        lastClick = 0
        settings = {"toggleKey": "²", # the key to toggle the trigger bot, the square on the frame is the state (red=disabled)
                    "cooldown": 1.1, # cooldown between click in seconds (only for mode 0)
                    "detect": [1], # detect enemybody [0] or enemyhead [1] and [0, 1] for both
                    "triggerDelay": 0} # delay between clicking on the target in seconds, 0 is fine 
        with mss() as stc:
            while True:
                closestPartDistance = 100000
                closestPart = -1

                currentTime = time.time()
                screenshot = np.array(stc.grab(region))
                screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

                frame = model.predict(screenshot, save=False, classes=settings["detect"], verbose=False, device=0, half=False)

                positionsFrame = pd.DataFrame(frame[0].cpu().numpy().boxes.data, columns=['xmin', 'ymin', 'xmax', 'ymax', 'conf', 'class'])

                for i, row in enumerate(positionsFrame.iterrows()):
                    try:
                        xmin, ymin, xmax, ymax, confidence, category = row[1].astype('int')
                        centerX = (xmax-xmin)/2+xmin
                        centerY = (ymax-ymin)/2+ymin
                        distance = math.dist([centerX, centerY], screenshotCenter)

                        if int(distance) < closestPartDistance:
                            closestPartDistance = distance
                            closestPart = i

                        cv2.rectangle(screenshot, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
                    except:
                        print("", end="")

                if keyboard.is_pressed(settings["toggleKey"]) and currentTime - lastClick > 0.2:
                    triggerbot = not triggerbot
                    lastClick = currentTime
                    print(triggerbot)

                if closestPart != -1:
                    xmin = positionsFrame.iloc[closestPart, 0]
                    ymin = positionsFrame.iloc[closestPart, 1]
                    xmax = positionsFrame.iloc[closestPart, 2]
                    ymax = positionsFrame.iloc[closestPart, 3]
                    inRange = screenshotCenter[0] in range(int(xmin),int(xmax)) and screenshotCenter[1] in range(int(ymin),int(ymax))
                    if currentTime - lastClick > settings["cooldown"] and triggerbot == True and inRange:
                        time.sleep(settings["triggerDelay"])
                        print(round(time.time() * 1000 - currentTime * 1000), " ms to trigger")
                        pyautogui.click() 
                        lastClick = currentTime
                    

                cv2.rectangle(screenshot, (0, 0), (20, 20), (0, 255, 0) if triggerbot else (0, 0, 255), -1)
                cv2.putText(screenshot, "ow-vision", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
                cv2.imshow("frame",screenshot)
                if(cv2.waitKey(1) == ord('l')):
                    cv2.destroyAllWindows()
                    break