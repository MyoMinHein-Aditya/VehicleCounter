from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing import process_image
from detector import VehicleDetector
from counter import count_vehicles
from utils import draw_boxes, encode_image

app = Flask(__name__)
CORS(app)

detector = VehicleDetector()

@app.route('/count', methods=['POST'])
def count_api():
    try:
        if 'image' not in request.files:
            raise ValueError("Please upload an image.")
            
        img = process_image(request.files['image'])
        detections = detector.detect(img)
        counts = count_vehicles(detections)
        
        annotated_img = draw_boxes(img, detections)
        img_base64 = encode_image(annotated_img)
        
        return jsonify({
            "counts": counts,
            "image": img_base64
        })
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)