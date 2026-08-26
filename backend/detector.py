from ultralytics import YOLO

class VehicleDetector:
    def __init__(self, model_path='yolov8m.pt'):
        self.model = YOLO(model_path)
        self.target_classes = {2: 'car', 3: 'motorcycle'}

    def detect(self, img, conf=0.30, iou=0.65, imgsz=1024):
        results = self.model.predict(img, classes=[2, 3], imgsz=imgsz, conf=conf, iou=iou)
        
        detections = []
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            detections.append({
                "class": self.target_classes[cls_id],
                "confidence": confidence,
                "bbox": [x1, y1, x2, y2]
            })
            
        return detections