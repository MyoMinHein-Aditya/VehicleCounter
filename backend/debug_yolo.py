from ultralytics import YOLO

model = YOLO('yolov8m.pt')
imgs = [
    r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413682.jpg',
    r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413702.jpg'
]

print("--- TESTING ALL CLASSES (NO FILTER) ---")
results = model.predict(imgs, conf=0.1, iou=0.8, imgsz=1024)
for i, r in enumerate(results):
    print(f"\nImage {i+1}:")
    counts = {}
    for box in r.boxes:
        cls_name = model.names[int(box.cls[0])]
        counts[cls_name] = counts.get(cls_name, 0) + 1
    print(counts)
