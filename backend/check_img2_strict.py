from ultralytics import YOLO

model = YOLO('yolov8m.pt')
img_path = r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413702.jpg'

print(f"Testing on Image 2: {img_path}")
for conf in [0.35, 0.45, 0.55, 0.60]:
    for iou in [0.20, 0.30, 0.45]:
        res = model.predict(img_path, classes=[2, 3, 5, 7], imgsz=640, conf=conf, iou=iou, verbose=False)
        boxes = res[0].boxes
        
        counts = {}
        for box in boxes:
            cls = int(box.cls[0])
            name = model.names[cls]
            counts[name] = counts.get(name, 0) + 1
            
        print(f"conf={conf:.2f}, iou={iou:.2f} -> Detections: {len(boxes)} | Counts: {counts}")
