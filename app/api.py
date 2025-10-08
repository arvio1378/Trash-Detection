from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from app.utils.detect_img import detect_image
from app.utils.detect_video import detect_video
from app.utils.categories import categories
import tempfile
import uvicorn

# FastAPI Initialization
app = FastAPI(
    title="Trash Detection API",
    description="An API for detecting trash items in images and videos using YOLOv8.",
    version="1.0.0"
)

# Load YOLOv8 Model
model = YOLO(r"runs\detect\train\weights\best.pt")

# home route
@app.get("/")
async def home():
    return {
        "message": "Welcome to the Trash Detection API. Use /detect-image or /detect-video endpoints to detect trash items."
    }

# detect image route
@app.post("/detect-image/")
async def detect_image_endpoint(file: UploadFile = File(...)):
    try:
        # save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name
        
        # perform detection
        results = detect_image(temp_file_path, model)

        detected_items = []

        for cls, count in results["class_counts"].items():
            category, color, emoji, info = categories.get(cls, ("Unknown", "black", "❓", "information not available"))
            detected_items.append({
                "class": cls,
                "count": count,
                "category": category,
                "color": color,
                "emoji": emoji,
                "info": info
            })
        
        return JSONResponse(content={
            "status": "success",
            "detected_items": detected_items
        })
    
    except Exception as e:
        return JSONResponse(content={
            "status": "error",
            "message": str(e)
        }, status_code=500)

# detect video route
@app.post("/detect-video/")
async def detect_video_endpoint(file: UploadFile = File(...)):
    try:
        # save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name
        
        # perform detection
        results = detect_video(temp_file_path, model)

        detected_items = []

        for cls, count in results["class_counts"].items():
            category, color, emoji, info = categories.get(cls, ("Unknown", "black", "❓", "information not available"))
            detected_items.append({
                "class": cls,
                "count": count,
                "category": category,
                "color": color,
                "emoji": emoji,
                "info": info
            })
        
        return JSONResponse(content={
            "status": "success",
            "detected_items": detected_items
        })
    
    except Exception as e:
        return JSONResponse(content={
            "status": "error",
            "message": str(e)
        }, status_code=500)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)