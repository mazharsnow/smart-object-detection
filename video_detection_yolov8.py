import cv2
import os
import time
from ultralytics import YOLO

# Paths
input_video = "Input Frame/walking.mp4"
output_dir = "Output Frame"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "output_walking.mp4")

# Load YOLOv8 model (tiny version for speed; you can switch to yolov8s.pt etc.)
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    raise FileNotFoundError(f"Could not open video: {input_video}")

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_input = int(cap.get(cv2.CAP_PROP_FPS))

# Define video writer for output
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps_input, (frame_width, frame_height))

font = cv2.FONT_HERSHEY_SIMPLEX
start_time = time.time()
frame_count = 0

print("🎬 Processing video... press ESC to quit early.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Run YOLOv8 detection
    results = model(frame, verbose=False)
    result = results[0]

    # Draw detections
    annotated_frame = result.plot()

    # Calculate FPS
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (10, 40),
        font,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )

    # Display frame
    cv2.imshow("YOLOv8 Video Detection", annotated_frame)

    # Save to output video
    out.write(annotated_frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"\n✅ Processing complete! Output saved to: {output_path}")
