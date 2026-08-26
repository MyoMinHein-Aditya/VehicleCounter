# Vehicle Counter

A web application that detects, counts, and highlights cars and motorcycles in dense images using a YOLOv8 machine learning model.

### Features
* Upload images through a clean web interface.
* Utilizes the YOLOv8 Medium model for high accuracy.
* Specifically optimized to handle dense traffic and overlapping vehicles.
* Filters detections strictly for cars and motorcycles.
* Returns exact counts and an annotated image with bounding boxes.

### Prerequisites
* Python 3.8 or higher.
* A modern web browser.

### Installation
* Clone or download this project folder to your local machine.
* Open your terminal and navigate to the project folder.
* Create a virtual environment using `python -m venv venv`.
* Activate the virtual environment:
  * Windows: `venv\Scripts\activate`
  * Mac/Linux: `source venv/bin/activate`
* Install the required dependencies using `pip install -r requirements.txt`.

### Usage
* Start the backend server by running `python app.py` in your terminal.
* Wait for the server to start (it will run on `http://localhost:5000`).
* Open the `index.html` file directly in your web browser.
* Upload an image of a parking lot and click "Analyze Image".

### Project Structure
* `app.py`: The Flask backend API that handles image processing and YOLOv8 inference.
* `index.html`: The frontend user interface for uploading images and displaying results.
* `requirements.txt`: The list of Python dependencies required to run the project.