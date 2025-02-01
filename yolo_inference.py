from ultralytics import YOLO

model = YOLO('yolo11m')

results = model.predict('input_videos/test.mp4',save=True)
print(results[0]) # 1st frame

print("++++++++++++++++++++++++++++++")
for box in results[0].boxes: # Loop through all the frames
    print(box)