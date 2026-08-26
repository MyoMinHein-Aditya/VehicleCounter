from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import numpy as np
import base64

app = Flask(__name__)
CORS(app)

model = YOLO('yolov8m.pt')

@app.route('/count',methods=['POST'])
def count_vehicles():
    if 'image' not in request.files:
        return jsonify({"error":"No image uploaded"}), 400

    file = request.files['image']
    img_bytes = file.read()
    nparr = np.frombuffer(img_bytes , np.uint8)
    img = cv2.imdecode(nparr , cv2.IMREAD_COLOR)

    results = model.predict(img, classes=[2 , 3], imgsz = 1024, conf = 0.15, iou = 0.65)

    car_count = 0
    moto_count = 0

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        if cls_id == 2:
            car_count += 1
        elif cls_id == 3:
            moto_count += 1

    plotted_img = results[0].plot()
    _, buffer = cv2.imencode('.jpg',plotted_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return jsonify({
        "cars":car_count,
        "motorcycles":moto_count,
        "total": car_count + moto_count,
        "image":img_base64
    })

if __name__ == '__main__':
    app.run(debug = True, port = 5000)