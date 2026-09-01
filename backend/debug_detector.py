import cv2
from detector import VehicleDetector
from counter import count_vehicles

detector = VehicleDetector()

imgs = [
    r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413682.jpg',
    r'C:/Users/adity/.gemini/antigravity/brain/d7f9c910-cd00-4eb6-accc-db9e6d31138d/.user_uploaded/media_1788261413702.jpg'
]

for i, p in enumerate(imgs):
    img = cv2.imread(p)
    dets = detector.detect(img)
    counts = count_vehicles(dets)
    print(f"Image {i+1} counts: {counts}")
