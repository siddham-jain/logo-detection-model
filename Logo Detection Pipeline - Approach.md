# Logo Detection Pipeline - Approach

##### Problem Statement:
To make a ML pipeline which detects logo of pepsi and coca cola from a video and returns timestamp in `JSON` format

##### My Approach:
-> To extract video frames I used `av` python library as mentioned in the assignment doc
-> It was decided that we are required to train a `YOLO` model, version of our choice
-> I used `YOLOv8` for logo detection.
-> Used AdamW optimizer with learning rate of 0.0016 and momentum of 0.9
-> Wrote a basic python script to extract video frames and then pass it to the model
###### WHY `YOLOv8`? 
My choice boiled down to three `YOLO` version `v8`, `v9`, `v10` because there was a significant improvement in both performance and accuracy from `v3` to `v8` trained on COCO dataset. 

Take a look at below images which i got stumbled upon while researching for the best model for my use case:-
![Alt text](https://i.imgur.com/WvNsXJs.png)
Image Credits:- https://youtu.be/x20MxX-AWzE?si=peWs1ppEaBbdypLu

- `YOLOv8` is better than `YOLOv10` in detecting instances of smaller objects which makes `YOLOv8` a better option than `v10` for our use case
- `YOLOv8` comes with the drawback of potentially detecting non-existent objects, leading to a increase in false positive instances.
- `YOLOv8` has better segmentation abilities while `YOLOv9` primarily focuses on object detection.
- To overcome that we can use dual model approach in which `YOLOv8` is used for logo detection and `EfficientNet, EfficientDet or MobileNet` for logo classification to remove false positive instances of detected logo.

-> After deciding to use `YOLOv8`, the next step involves determining the optimal weights for fine-tuning the model.
-> I have chosen `YOLOv8s` for my model

###### Why `YOLOv8s`?
![Alt text](https://i.imgur.com/hsOzmeN.png)

- Balance of speed and accuracy: On A100 GPU, it operates on 1.20ms per inference which makes it faster when we will use our model for logo detection in real time.
- It has a mAP of 44.9 which is higher than `v8n`, lower than `v8x`, but is a goof trade off for speed per inference.
- Resource Efficiency: It has 11.2m params which are fewer than other models but making it consume less computational resources and best choice for me.
- Basically the balance between speed, accuracy and resource efficiency convinced me to use `YOLOv8s` for tuning my model.

##### Problems faced during the assignment
The only thing that stopped me from making a production-ready model was computational resources—just kidding, I've got this!
Somehow my model managed to achieved following metrics:-
- precision: 0.79
- speed: 0.3ms preprocess, 4.8ms inference, 0.0ms loss, 4.8ms postprocess per image
- recall: 0.788
- mAP50: 0.834
- mAP50-95: 0.582

**Challenges:**
![Alt text](https://i.imgur.com/LjjpdXF.png)

- Dataset of coca-cola was not up to the mark that's why there is a significant difference between the metrics of both the classes.

![ALt text](https://i.imgur.com/vKQolK6.png)

- When I tried to run my script on the original video, my VS Code crashed due to insufficient resources. After trimming the video to one minute in length, the script ran successfully.

##### Conclusion
In this project I have successfully implemented a YOLOv8s-based model for Pepsi and Coca-Cola logo detection in video streams. While there is room for improvement, particularly in balancing class performance and optimizing resource usage, this implementation lays down a solid foundation for real-time logo detection.

Future work will focus on expanding the dataset, refining the model architecture, and enhancing overall system efficiency to address the challenges and further improve performance.
