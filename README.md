# Trash-Detection

## 📋 Overview
Trash Detection adalah proyek berbasis computer vision yang bertujuan untuk mendeteksi dan mengklasifikasikan jenis sampah menggunakan model YOLO (You Only Look Once). Proyek ini mendukung pengelolaan sampah cerdas dengan mendeteksi objek seperti plastic, metal, cardboard, battery, can, bulb, dan lain-lain secara real-time dari gambar atau video.

## 🚀 Fitur
- Deteksi otomatis berbagai jenis sampah
- Menggunakan model YOLOv8 untuk performa cepat dan akurat
- Visualisasi hasil pelatihan: precision, recall, F1-score, confusion matrix, dan PR curve
- Antarmuka Streamlit untuk upload gambar dan melihat hasil deteksi
- Warna label berbeda untuk setiap kategori sampah

## 🧩 Tools & Library
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

## Training Model
Parameter train yolo yang digunakan :
```bash
model.train(
        data="dataset\data.yaml",
        epochs=50,       
        imgsz=640,
        batch=8,
        device=0,
        workers=2
    )
```

## 📊 Evaluation Metrics
Beberapa metrik hasil training:
- Precision-Confidence
<img width="1564" height="1042" alt="image" src="https://github.com/user-attachments/assets/bd83795d-f16b-40a6-81ff-baee0c3899fa" />
Presisi meningkat seiring meningkatnya keyakinan dan presisi rata-rata dapat mencapai 0,99 (sangat akurat).

- Recall-Confidence
<img width="1434" height="956" alt="image" src="https://github.com/user-attachments/assets/7e85b03c-4fa2-4b2e-b4b8-450c34d494cb" />
Daya ingat tinggi (0,96) saat ambang batas rendah. Seiring meningkatnya ambang batas, daya ingat menurun.

- F1-Confidence
<img width="1434" height="956" alt="image" src="https://github.com/user-attachments/assets/9f3a9877-7a68-42b8-b8d0-0515d93be9d9" />
Menunjukkan keseimbangan Presisi & Ingatan pada berbagai tingkat keyakinan. F1 tertinggi = 0,87 pada ambang batas 0,59, titik optimal untuk inferensi

- Confusion Matrix
<img width="1659" height="1244" alt="image" src="https://github.com/user-attachments/assets/b4586863-b1b4-4e3e-a670-b864a31b42ee" />
Mayoritas prediksi benar. Kelas yang mudah dideteksi: baterai, botol plastik, tutup botol plastik. Kelas yang sulit: kantong plastik, kardus, gelas kaca (sering keliru digunakan sebagai latar belakang).

## 🏗️ Kontribusi
Dapat melakukan kontribusi kepada siapa saja. Bisa bantu untuk :
- Menambahkan lebih banyak dataset
- Pengoptimalan kinerja model
- Integrasi dengan IoT Smart Bin

## 🧑‍💻 Tentang Saya
Saya sedang belajar dan membangun karir di bidang AI/ML. Projek ini adalah latihan saya untuk membangun aplikasi python sederhana. Saya ingin lebih untuk mengembangkan skill saya di bidang ini melalui projek-projek yang ada.
📫 Terhubung dengan saya di:
- Linkedin : https://www.linkedin.com/in/arvio-abe-suhendar/
- Github : https://github.com/arvio1378
