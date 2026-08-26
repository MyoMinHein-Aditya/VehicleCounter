# Vehicle Detection and Counting System

A robust, image-based vehicle detection architecture that processes multiple image formats, detects cars and motorcycles using YOLOv8, and returns class-wise counts with an annotated bounding-box image.

### Problem
Monolithic detection scripts mix API routing, image processing, model inference, and counting logic, making them difficult to evaluate, scale, or maintain.

### Objective
To build a production-ready, modular computer vision pipeline with strict separation of concerns between the API layer, preprocessing, detection, counting, and utilities.

### Architecture

             IMAGE
               |
        PREPROCESSING
               |
          YOLO MODEL
               |
       +-------+-------+
       |               |
      CAR         MOTORCYCLE
       |               |
       +-------+-------+
               |
         COUNT + BOXES
               |
          FINAL IMAGE

### Model Details
* Base Model: YOLOv8 Medium (yolov8m.pt)
* Target Classes: Car (2), Motorcycle (3)
* Confidence Threshold: 0.30 (Tuned for density)
* NMS IoU Threshold: 0.65
* Inference Image Size: 1024

### Supported Formats
* JPEG / JPG
* PNG
* WEBP
* BMP
* TIFF

### Prerequisites
* Python 3.14.2
* pip or uv package manager

### Installation
1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Ensure `models/yolov8m.pt` is downloaded (the script will auto-download on first run if missing).

### Usage
1. Open a terminal in the project root.
2. Run `python backend/app.py`.
3. Open `frontend/index.html` in your web browser.
4. Upload an image to view the extracted counts and bounding boxes.

### Evaluation Metrics
* Precision, Recall, and mAP@50 metrics are calculated via the testing suite.
* Run `pytest tests/` to execute image validation, detection response, and counting logic tests.

### Limitations
* Extremely dense occlusion may still merge distant vehicles.
* High-angle, bird's-eye view cameras might require a custom-trained model or SAHI integration.

### Future Improvements
* Integrate SAHI for high-density slicing.
* Fine-tune the model specifically on the India Driving Dataset (IDD).
* Add a database layer to track counts over time.