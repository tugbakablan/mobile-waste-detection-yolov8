from ultralytics import YOLO

model_path = "model/best_model.pt"
image_path = "images/sampleimage.jpeg"
output_path = "images/output.jpg"

model = YOLO(model_path)

results = model(image_path)
results[0].save(output_path)

print(f"Prediction saved to {output_path}")
