# Mobile Waste Detection with YOLOv8n
This repository presents an end-to-end waste detection system designed for mobile devices.
The system performs real-time object detection using YOLOv8 and is optimized for on-device inference.
The project covers the full pipeline from dataset creation and model selection to mobile deployment.

## Model Selection

7  object detection models were trained and evaluated under identical conditions. Then,new datas added and two best-performed model re-trained.
The selection was based on accuracy, speed, and suitability for real-time mobile deployment. 
<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/0ffed436-e4eb-431d-a6dc-ea34fe37feba" />
<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/f7b121c2-516c-46f0-bc1a-21c828550dd5" />

YOLOv8n was selected as the final model due to its superior real-time performance and highest overall efficiency score for mobile inference.

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

### Mobile Application Inference
Examples of real-world detections produced by the final YOLOv8n model.

<img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/9f4b8dd5-029b-46cb-b062-3c94ef387a93" /><img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/ef922eee-54df-41d6-b470-af01d530c441" /><img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/8793b840-a7ef-481a-a939-17819318f520" /><img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/05a07e31-cd3e-4d7f-8f75-89cf974717a3" />



