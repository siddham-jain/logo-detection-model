import json
import av
import numpy as np

# function to extract frames from video
def extract_frames(video_path):
    container = av.open(video_path)
    frames = []
    for frame in container.decode(video=0):
        timestamp = float(frame.pts * frame.time_base)
        img = frame.to_image()
        frames.append((img, timestamp))
    return frames

# function to generate output json
def output_generator(pepsi_pts, cocacola_pts, output_path='output.json'):
    output = {
        "Pepsi_pts": [ {k: convert(v) for k, v in entry.items()} for entry in pepsi_pts ],
        "CocaCola_pts": [ {k: convert(v) for k, v in entry.items()} for entry in cocacola_pts]
    }
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=4)

# function to convert non-serializable objects to serializable objects
def convert(data):
    if isinstance(data, (list, dict)):
        return data
    elif hasattr(data, 'tolist'):
        # converting numpy array to tensors
        return data.tolist()  
    elif hasattr(data, 'item'):
        # converting tensor to scalar
        return data.item()  
    else:
        # converting other non-serializable objects to string
        return str(data)  

 # function to calculate size of bounding box       
def calculate_size(x1, y1, x2, y2):
    return {"width": format(x2 - x1), "height": format(y2 - y1)}

# function to calculate distance of bounding box from center
def calculate_distance_from_center(x1, y1, x2, y2, frame_width, frame_height):
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    frame_center_x = frame_width / 2
    frame_center_y = frame_height / 2
    # distance = sqrt((x2-x1)^2 + (y2-y1)^2)
    distance_from_center = ((center_x - frame_center_x) ** 2 + (center_y - frame_center_y) ** 2) ** 0.5 # using simple distance formula
    return distance_from_center

def format(x):
    return np.round(x, 3)
