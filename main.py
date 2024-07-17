from ultralytics import YOLO
from PIL import Image
import sys
from utils import extract_frames, calculate_distance_from_center, calculate_size, format, output_generator

output_path = 'output.json'
model_path = 'model/best.pt'


model = YOLO(model_path)  # loding my custom model

threshold = 0.4 # defining a confidence threshold


def detect_logos(frames):
    pepsi_pts = []
    cocacola_pts = []

    frames = frames[:10] # limiting the number of frames to 10 for testing purposes

    for img, timestamp in frames:
        results = model(img)  # running an inference
        
        for result in results:
            boxes = result.boxes  # boxes object

            for box in boxes:
                score = box.conf[0].item()  # getting confidence score

                if score > threshold:
                    class_id = int(box.cls[0].item())  # getting class id to define weather it is pepsi or cocacola
                    x1, y1, x2, y2 = box.xyxy[0].tolist()  # getting coordinates of bounding box
                    class_name = result.names[class_id].lower()
                    size = calculate_size(x1, y1, x2, y2)
                    distance_from_center = calculate_distance_from_center(x1, y1, x2, y2, img.width, img.height)

                    # formatting the output to 2 decimal places
                    info = {
                        "timestamp": format(timestamp),
                        "distance_from_center": format(distance_from_center),
                        "size": size
                    }
                    
                    # appending the info to the respective list
                    if class_name == 'pepsi':
                        pepsi_pts.append(info)
                    elif class_name == 'coca-cola':
                        cocacola_pts.append(info)

    return pepsi_pts, cocacola_pts

def main(video_path):
    frames = extract_frames(video_path)
    pepsi_pts, cocacola_pts = detect_logos(frames)
    output_generator(pepsi_pts, cocacola_pts, output_path)

if __name__ == "__main__":
    if len(sys.argv) < 2: # check to enusre that video path is provided
        print("Please provide video path as an argument")
        sys.exit(1)
    video_path = sys.argv[1]
    main(video_path)
