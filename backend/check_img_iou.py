from ultralytics import YOLO

model = YOLO('yolov8m.pt')
img2 = r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413702.jpg'
img1 = r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413682.jpg'

for conf in [0.40, 0.45, 0.50]:
    for iou in [0.10, 0.15, 0.20]:
        res = model.predict(img2, classes=[2, 3, 5, 7], imgsz=640, conf=conf, iou=iou, verbose=False)
        boxes = res[0].boxes
        counts = {}
        for box in boxes:
            cls = int(box.cls[0])
            name = model.names[cls]
            counts[name] = counts.get(name, 0) + 1
        print(f"Img2 - conf={conf}, iou={iou} -> {len(boxes)} | {counts}")

        res1 = model.predict(img1, classes=[2, 3, 5, 7], imgsz=640, conf=conf, iou=iou, verbose=False)
        print(f"Img1 - conf={conf}, iou={iou} -> {len(res1[0].boxes)}")
