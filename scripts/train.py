from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
import os

cwd = os.getcwd()
print(cwd)

if __name__ == '__main__':
    model.train(data='./data.yaml', epochs=150, imgsz=640, device=0)