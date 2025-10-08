from ultralytics import YOLO

def main():
    model = YOLO("yolov8s.pt")
    model.train(
        data="dataset\data.yaml",
        epochs=50,       
        imgsz=640,
        batch=8,
        device=0,
        workers=2
    )

if __name__ == "__main__":
    main()