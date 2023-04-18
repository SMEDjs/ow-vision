import cv2
import os

if __name__ == "__main__":
    projectFolder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    videoFolder = os.path.join(projectFolder, "videos", "clip")
    exportFolder = os.path.join(projectFolder, "videos", "exportedFrames")
    print(videoFolder)

    os.chdir(exportFolder)
    MONITOR_WIDTH = 1920
    MONITOR_HEIGHT = 1080
    MONITOR_SCALE = 5

    region = (int(MONITOR_WIDTH/2-MONITOR_WIDTH/MONITOR_SCALE/2),int(MONITOR_HEIGHT/2-MONITOR_HEIGHT/MONITOR_SCALE/2),int(MONITOR_WIDTH/2+MONITOR_WIDTH/MONITOR_SCALE/2),int(MONITOR_HEIGHT/2+MONITOR_HEIGHT/MONITOR_SCALE/2))
    x,y,width,height = region

    for video_name in os.listdir(videoFolder):
        vidcap = cv2.VideoCapture(videoFolder+"\\"+video_name)
        success, image = vidcap.read()
        count = 0
        frame = 0   
        while success:
            frame += 1
            success, image = vidcap.read()
            if (frame % 20 == 0):
                image = image[y:height,x:width]
                cv2.imwrite(video_name+"frame%d.jpg" % count, image)   
                success, image = vidcap.read()
                print('Read frame ', frame)
                count += 1