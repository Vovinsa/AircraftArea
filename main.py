from ultralytics import YOLO

import json
import argparse

from src.predictor import Predictor


parser = argparse.ArgumentParser(description='Assaia parser')
parser.add_argument('--video-path', type=str)
parser.add_argument('--polygon-path', type=str)
parser.add_argument('--output-path', type=str, default=1)

if __name__ == '__main__':
    args = parser.parse_args()

    video_path = args.video_path
    polygon_path = args.polygon_path
    output_path = args.output_path

    model = YOLO('models/yolov8l.pt')
    predictor = Predictor(model=model)

    with open(polygon_path) as f:
        polygon = json.load(f)

    _, intervals = predictor.predict_vehicle_entity(
        video_path=video_path,
        polygon=list(polygon.values())[0]
    )

    result = {list(polygon.keys())[0]: intervals}

    with open(output_path, 'w') as f:
        json.dump(result, f)
