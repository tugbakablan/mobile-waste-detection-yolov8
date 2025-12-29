# Real-Time Waste Detection on Mobile Devices
<img width="300" height="420" alt="image" src="https://github.com/user-attachments/assets/6723f5ab-fa94-4d7d-991b-e3f7115eed0a" />

This project presents an end-to-end real-time waste detection system designed for mobile devices.
A custom dataset was created from scratch and object detection models YOLOv8s/n, YOLOv11s/n, YOLOv12s/n, RT-DETR were trained and evaluated under identical conditions.
Through data-centric optimization, YOLOv8n was selected as the final model, achieving 0.9248 mAP50
and 91.42 FPS, and deployed on a mobile application using TensorFlow Lite.

<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/0ffed436-e4eb-431d-a6dc-ea34fe37feba" />

## Dataset

The dataset used in this project was created specifically for this study.
Images were collected from real-world environments and on Roboflow, manually annotated
with bounding boxes for waste categories such as plastic, paper, glass, and metal.

The dataset is not publicly released due to licensing and privacy considerations.
However, representative samples and annotation examples are provided above.

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


Although RT-DETR achieved the highest and YOLOv12 achieved similar accuracy, its inference speed was not suitable
for real-time mobile applications. YOLOv8n provided the best balance between accuracy
and speed, outperforming other models with a significantly higher FPS while maintaining
competitive detection performance. Therefore, YOLOv8n was selected as the final model
for mobile deployment.

## Mobile Application Inference
Examples of real-world detections produced by the final YOLOv8n model.

<img width="1115" height="545" alt="image" src="https://github.com/user-attachments/assets/3d3ee4d2-288c-4ae4-ad6f-7b551350f344" />

## Conclusion

This project demonstrates a complete mobile-oriented object detection pipeline,
from dataset creation and model benchmarking to real-time deployment.
By prioritizing both accuracy and inference speed, the final system achieves
practical usability on resource-constrained mobile devices.
