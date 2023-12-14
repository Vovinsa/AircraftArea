# Overview

This system is equipped with a stationary camera strategically positioned to observe the designated area where aircraft are prepared for departure. The primary objective is to ensure the absence of any vehicles within the stand boundary before the aircraft arrives. In the event of detecting any vehicles within this zone, the system is designed to promptly notify the ground handler for immediate action

---

# Approach

In this setup, I'm not training a new model. Instead, I'm using an existing model called YOLOv8 for spotting vehicles in videos. YOLOv8 is designed to identify objects in images or video frames. I'm applying this model to each frame of the input videos (like video_0.mp4, video_1.mp4) to locate vehicles and draw bounding boxes around them.

Here's the trick: I'm not going through the hassle of training my own model because it's resource-intensive. Instead, I'm relying on the YOLOv8 model that's already been trained.

Once the vehicles are identified, I'm checking whether they fall within a specific polygonal boundary. This boundary represents the designated area where vehicles should or should not be present, like the stand area for an aircraft

---

# Metrics

Precision and recall are commonly used metrics in binary classification tasks, and they are particularly relevant for evaluating the performance of a system designed to monitor and notify the presence of vehicles on the aircraft stand. Let's delve into the reasons for choosing precision and recall and how they align with the task:

1. **Precision:**
   - Precision is the ratio of true positive predictions to the total number of positive predictions (true positives + false positives).
   - In the context of the aircraft stand monitoring system, precision is crucial because it measures the accuracy of the system in identifying and alerting about vehicles on the stand. A high precision value indicates that when the system notifies the ground handler, it is likely to be correct and that there are indeed vehicles present.

2. **Recall:**
   - Recall, also known as sensitivity or true positive rate, is the ratio of true positive predictions to the total number of actual positive instances (true positives + false negatives).
   - Recall is significant in this task as it gauges the system's ability to capture and identify all instances of vehicles on the stand. A high recall value implies that the system is effective in minimizing false negatives, ensuring that it reliably detects and notifies the ground handler whenever a vehicle is present.

In the context of the aircraft stand monitoring system:

- **False Positives (FP):** Predicting a vehicle is present when it is not.
- **False Negatives (FN):** Failing to predict a vehicle that is present.

Here's how precision and recall relate to the task:

- **High Precision:** Indicates a low rate of false positives. The ground handler can trust the system's alerts, as they are likely accurate.
  
- **High Recall:** Signifies a low rate of false negatives. The system consistently detects vehicles on the stand, reducing the risk of missing any instances.

Balancing precision and recall is often essential, as there is typically a trade-off between the two. Depending on the system's requirements and priorities, one may need to adjust the model or algorithm parameters to achieve the desired balance between minimizing false positives and false negatives.

Below are the evaluation metrics for the aircraft stand monitoring system applied to different video files. The metrics include precision and recall values for each video, providing insights into the system's performance in identifying and notifying the presence of vehicles on the aircraft stand

- **video_11.mp4**
Precision: 1.0
Recall: 1.0
- **video_13.mp4**
Precision: 0.4237
Recall: 1.0
- **video_16.mp4**
Precision: 0.5333
Recall: 1.0
- **video_17.mp4**
Precision: 0.1569
Recall: 1.0
- **video_8.mp4**
Precision: 0.0
Recall: 0.0
- **video_15.mp4**
Precision: 1.0
Recall: 0.9
- **video_14.mp4**
Precision: 0.0615
Recall: 1.0
- **video_9.mp4**
Precision: 0.0
Recall: 0.0
- **video_4.mp4**
Precision: 0.5152
Recall: 1.0
- **video_19.mp4**
Precision: 0.3709
Recall: 0.9825
- **video_18.mp4**
Precision: 1.0
Recall: 1.0
- **video_5.mp4**
Precision: 0.2378
Recall: 1.0
- **video_7.mp4**
Precision: 1.0
Recall: 0.7597
- **video_6.mp4**
Precision: 0.8906
Recall: 0.9913
- **video_2.mp4**
Precision: 0.8571
Recall: 0.75
- **video_3.mp4**
Precision: 0.1455
Recall: 1.0
- **video_1.mp4**
Precision: 1.0
Recall: 0.3333
- **video_0.mp4**
Precision: 0.0
Recall: 0.0

These metrics offer a detailed assessment of the system's ability to accurately identify the presence of vehicles on the stand. While the results indicate notable performance in certain cases, it's important to note that due to resource limitations, model improvements, such as employing a larger model, are currently unfeasible. Ongoing efforts will focus on optimizing within the existing resource constraints for enhanced precision and recall across all scenarios

---

# Inference

To run inference run the command below:

```bash
bash run.sh VIDEO_PATH POLYGON_PATH OUTPUT_PATH
```

Output of the script is a json file
Below there is an example:

```json
{"video_name": [[0, 10], [20, 23]]}
```