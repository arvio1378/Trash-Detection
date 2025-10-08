from PIL import Image
import cv2
from collections import Counter

def detect_image(image_path, model, confidence_threshold=0.5):
    # open image
    image = Image.open(image_path)

    # perform detection
    results = model.predict(image, conf=confidence_threshold)

    # convert to rgb
    img_rgb = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)

    # take classes and counts
    class_names = results[0].names
    detected_classes = [class_names[int(cls)] for cls in results[0].boxes.cls]

    # count occurrences of each class
    class_counts = Counter(detected_classes)

    # return results as dictionary
    return {
        "img_rgb": img_rgb,
        "class_counts": class_counts,
    }