import cv2
import time
from collections import Counter

def detect_video(video, model, stframe=None, confidence_threshold=0.5):
    try:
        cap = cv2.VideoCapture(video)
        detected_classes = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model.predict(frame, conf=confidence_threshold)
            annotated_frame = results[0].plot()

            detected_classes.extend([
                results[0].names[int(cls)] for cls in results[0].boxes.cls
            ])

            if stframe is not None:
                stframe.image(annotated_frame, channels="BGR", use_container_width=True)

            time.sleep(0.03)

        cap.release()

        if not detected_classes:
            return {"class_counts": {}}
        return {"class_counts": Counter(detected_classes)}
    
    except Exception as e:
        return {"error": str(e)}
