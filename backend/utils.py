import cv2
import base64

def draw_boxes(img, detections):
    annotated_img = img.copy()
    
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        label = f"{det['class'].capitalize()} {det['confidence']:.2f}"
        
        color = (0, 255, 0) if det["class"] == "car" else (255, 165, 0) if det["class"] == "motorcycle" else (0, 0, 255)
        
        cv2.rectangle(annotated_img, (x1, y1), (x2, y2), color, 2)
        
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(annotated_img, (x1, y1 - 20), (x1 + tw, y1), color, -1)
        cv2.putText(annotated_img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        
    return annotated_img

def encode_image(img):
    _, buffer = cv2.imencode('.jpg', img)
    return base64.b64encode(buffer).decode('utf-8')