# Trash-Detection

## 📋 Overview
Trash Detection adalah proyek berbasis computer vision yang bertujuan untuk mendeteksi dan mengklasifikasikan jenis sampah menggunakan model YOLO (You Only Look Once). Proyek ini mendukung pengelolaan sampah cerdas dengan mendeteksi objek seperti plastic, metal, cardboard, battery, can, bulb, dan lain-lain secara real-time dari gambar atau video.

## 🚀 Fitur
- Deteksi otomatis berbagai jenis sampah
- Menggunakan model YOLOv8 untuk performa cepat dan akurat
- Visualisasi hasil pelatihan: precision, recall, F1-score, confusion matrix, dan PR curve
- Antarmuka Streamlit untuk upload gambar dan melihat hasil deteksi
- Warna label berbeda untuk setiap kategori sampah

## 🧠 Tools & Library
- Python
- Pandas
- YOLOv8
- Streamlit
- Counter
- PIL
- Time
- Tempfile
- CV2

## 📁 Struktur Folder
- Trash Detection/
  - app
      - utils
          - detect_img.py
          - detect_video.py
      - main.py
  - dataset
      - train
          - images
          - labels
      - test
          - images
          - labels
      - valid
          - images
          - labels
      - data.yaml
  - runs
      - detect
          - train
  - style
      - style.css
  - test.ipynb
  - train.py
  - requirements.txt
  - README.md
  - yolo11n.pt
  - yolov8s.pt

## 🖥️ Cara Menjalankan Program
1. Clone Repositori
```bash
git clone https://github.com/arvio1378/Trash-Detection.git
cd Trash-Detection
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Jalankan Program
```bash
streamlit run app/main.py
```
