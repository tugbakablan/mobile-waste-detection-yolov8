# Real-Time Waste Detection on Mobile Devices

This project presents an end-to-end real-time waste detection system designed for mobile devices.
A custom dataset was created from scratch and object detection models YOLOv8s/n, YOLOv11s/n, YOLOv12s/n, RT-DETR were trained and evaluated under identical conditions.
Through data-centric optimization, YOLOv8n was selected as the final model, achieving 0.9248 mAP50
and 91.42 FPS, and deployed on a mobile application using TensorFlow Lite.

<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/0ffed436-e4eb-431d-a6dc-ea34fe37feba" />

## Dataset
The dataset used in this project was fully created from scratch by the authors.
All images were collected manually under real-world conditions and annotated using bounding boxes.

- Total images: 1686
- Classes: glass, paper, metal, plastic, organic
- Annotations: Manual bounding box labeling
- Train / Validation / Test split: 70% / 20% / 10%
  
  <img width="350" height="350" alt="image" src="https://github.com/user-attachments/assets/ee77bb5d-7872-4648-aa40-43249d70c0a7" />
  
  No pre-existing public waste dataset was used in this project.

### Data-Centric Improvements
Model performance improvements were primarily achieved through dataset refinement rather than architectural changes:

- Class balance optimization
- Data augmentation (rotation, brightness variation, blur)
- Iterative dataset versioning and error analysis

## Model Selection

7  object detection models were trained and evaluated under identical conditions. Then,new datas added and two best-performed model re-trained.
The selection was based on accuracy, speed, and suitability for real-time mobile deployment. 

<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/f7b121c2-516c-46f0-bc1a-21c828550dd5" />

YOLOv8n was selected as the final model due to its superior real-time performance and highest overall efficiency score for mobile inference.

### Mobile Application Inference
Examples of real-world detections produced by the final YOLOv8n model.

<img width="1115" height="545" alt="image" src="https://github.com/user-attachments/assets/3d3ee4d2-288c-4ae4-ad6f-7b551350f344" />




