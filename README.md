# 🧠 Smart Object Detection (YOLOv8)

Smart Object Detection is a modern, real-time object detection system powered by YOLOv8, OpenCV, and PyTorch. It detects multiple objects in both images and videos, displaying and saving annotated results automatically in dedicated folders.

## 🚀 Features

* 🖼️ Detect objects in images and videos
* ⚡ Real-time FPS tracking for video detection
* 💾 Automatically saves processed outputs in organized folders
* 🔍 Powered by Ultralytics YOLOv8 — the latest in real-time computer vision
* 🧰 Easy to customize and extend

## 📂 Folder Structure

```
smart-object-detection/
│
├── Input Frame/        # Place your input videos here
├── Input Images/       # Place your input images here
├── Output Frame/       # Processed videos with detection boxes
├── Output images/      # Processed images with bounding boxes
│
├── image_detection_yolov8.py   # Script for image detection
├── video_detection_yolov8.py   # Script for video detection
├── yolov8n.pt                  # YOLOv8 Nano weights
├── Requirements.txt            # Dependencies list
├── README.md                   # Documentation
└── .gitignore                  # Ignored files (e.g. venv, runs, media)
```

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mazharsnow/smart-object-detection.git
cd smart-object-detection
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r Requirements.txt
```

## 🧪 Usage

### 🔹 Image Detection

1. Place your image in the `Input Images` folder.
2. Run the script:

```bash
python image_detection_yolov8.py
```

3. The processed image will be saved in the `Output images` folder.

### 🔹 Video Detection

1. Place your video in the `Input Frame` folder.
2. Run the script:

```bash
python video_detection_yolov8.py
```

3. The processed video will be saved in the `Output Frame` folder. FPS and detection results will be displayed in real time.

## 📦 Requirements

* Python >= 3.8
* opencv>=4.10.0.84
* numpy>=1.26.3
* pandas>=2.2.3
* torch>=2.3.0
* ultralytics>=8.3.0
* matplotlib>=3.9.2
* scikit-learn>=1.5.2
* albumentations>=1.4.8

Install everything using:

```bash
pip install -r Requirements.txt
```

## 🧠 Technologies Used

| Library | Purpose |
|---------|---------|
| YOLOv8 (Ultralytics) | Object detection model |
| OpenCV | Image and video processing |
| PyTorch | Deep learning framework |
| NumPy / Pandas | Data handling |
| Matplotlib | Visualization (optional) |

## 📸 Example Results

| Input | Output |
|-------|--------|
| ![Input Image](https://github.com/mazharsnow/smart-object-detection/blob/master/Input%20Images/room.jpg) | ![Output Image](https://github.com/mazharsnow/smart-object-detection/blob/master/Output%20images/output_room.jpg) |

## 🧰 Future Enhancements

* Add object counting and tracking
* Integrate with webcam/live stream
* Add distance estimation and object measurement
* Deploy as a web app with Streamlit

## 👨‍💻 Author

**Mazharul Islam Tusar**  
📧 mazharul.tusar@outlook.com  
💻 GitHub: [@mazharsnow](https://github.com/mazharsnow)

## 🏷️ GitHub Topics

```
object-detection, yolov8, computer-vision, deep-learning, pytorch, opencv,
ultralytics, real-time-detection, ai-project, python
```

## 📜 License

This project is released under the MIT License — free to use, modify, and distribute with attribution.
