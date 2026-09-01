from ultralytics import YOLO

model = YOLO('yolov8m.pt')
imgs = [
    r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413682.jpg',
    r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413702.jpg'
]

for img_path in imgs:
    print(f"\n--- {img_path[-8:]} ---")
    res = model.predict(img_path, classes=[2, 3, 5, 7], imgsz=640, conf=0.25, iou=0.50)
    boxes = res[0].boxes
    print(f"Total detections: {len(boxes)}")
    for box in boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        name = model.names[cls]
        print(f"Detected {name} with conf {conf:.2f}")
