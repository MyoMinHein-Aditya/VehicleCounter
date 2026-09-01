import cv2
from ultralytics import YOLO

model = YOLO('yolov8m.pt')
img1 = cv2.imread(r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413682.jpg')

print("Grid search on image 1")
for imgsz in [640, 1024]:
    for conf in [0.1, 0.2, 0.3]:
        for iou in [0.4, 0.6, 0.8]:
            res = model.predict(img1, classes=[2, 3, 5, 7], imgsz=imgsz, conf=conf, iou=iou, verbose=False)
            print(f"imgsz={imgsz}, conf={conf}, iou={iou} -> count={len(res[0].boxes)}")
