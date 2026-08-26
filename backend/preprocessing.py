import cv2
import numpy as np

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(file_storage):
    if not file_storage or not file_storage.filename:
        raise ValueError("Please upload an image.")
    
    if not allowed_file(file_storage.filename):
        raise ValueError("Unsupported image format.")

    img_bytes = file_storage.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Unable to read or corrupt image.")

    return img