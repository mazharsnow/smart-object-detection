import cv2
import os
from ultralytics import YOLO

# Paths
input_path = "Input Images/room.jpg"
output_dir = "Output Images"
output_path = os.path.join(output_dir, "output_room.jpg")

# Ensure output folder exists
os.makedirs(output_dir, exist_ok=True)

# Load the YOLOv8 model (you can switch to yolov8s.pt, yolov8m.pt, etc.)
model = YOLO('yolov8n.pt')

# Load the image
img = cv2.imread(input_path)
if img is None:
    raise FileNotFoundError(f"Could not find image at {input_path}")

# Optional resize for faster inference
img = cv2.resize(img, None, fx=0.4, fy=0.4)

# Run object detection
results = model(img)

# Get first result (YOLOv8 returns a list)
result = results[0]

# Draw bounding boxes, labels, and confidence scores
annotated_img = result.plot()

# Show image
cv2.imshow("YOLOv8 Object Detection", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output to Output Images folder
cv2.imwrite(output_path, annotated_img)
print(f"✅ Output saved to: {output_path}")

# Print detection details
for box in result.boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    label = model.names[cls_id]
    print(f"Detected: {label} ({conf:.2f})")
