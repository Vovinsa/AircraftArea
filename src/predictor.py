import numpy as np
import cv2

from typing import Tuple, List

from .utils import is_box_inside_polygon, find_intervals


class Predictor:
    def __init__(self, model):
        self._model = model

    def predict_vehicle_entity(self, video_path: str, polygon: list) -> Tuple[List[int], List[List[int]]]:
        """
         Predicts the presence of vehicle entities inside a specified polygon region in a video.

         Parameters:
         - video_path (str): The path to the video file.
         - polygon (list): List of coordinates defining a polygon region.

         Returns:
         - Tuple[List[int], List[List[int]]]: A tuple containing two lists:
             - List[int]: Binary predictions (1 for presence, 0 for absence) for each timestamp in the video.
             - List[List[int]]: Intervals indicating consecutive frames with predicted vehicle entities.
         """
        frames = self._get_frames(video_path)
        outputs = self._model.predict(frames, verbose=False)
        h, w = frames[0].shape[:2]

        predictions = [0] * len(frames)

        for timestamp, out in enumerate(outputs):
            labels = out.boxes.cls.detach().cpu().numpy()

            boxes = out.boxes.xyxyn.detach().cpu().numpy()
            boxes[:, [0, 2]] *= w
            boxes[:, [1, 3]] *= h
            boxes = boxes.astype(np.int32)
            boxes = boxes[np.isin(labels, (2, 5, 6, 7))]

            for box in boxes:
                if is_box_inside_polygon(polygon, box):
                    predictions[timestamp] = 1
        return predictions, find_intervals(predictions)

    @staticmethod
    def _get_frames(video_path: str) -> List[np.ndarray]:
        """
         Retrieves frames from a video file.

         Parameters:
         - video_path (str): The path to the video file.

         Returns:
         - List[np.ndarray]: A list of NumPy arrays, where each array represents a video frame.
         """
        cap = cv2.VideoCapture(video_path)

        frames = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        cap.release()

        return frames