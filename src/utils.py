from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from typing import List


def point_in_polygon(point, polygon):
    """
    Check if a point is inside a polygon.

    Parameters:
    - point (tuple): A tuple representing the (x, y) coordinates of the point.
    - polygon (list): A list of vertices representing the polygon.

    Returns:
    bool: True if the point is inside the polygon, False otherwise.
    """
    point = Point(*point)
    polygon = Polygon(polygon)
    return polygon.contains(point)


def is_box_inside_polygon(polygon: list, bbox: list) -> bool:
    """
    Check if a bounding box is entirely inside a polygon.

    Parameters:
    - polygon (list): A list of vertices representing the polygon.
    - bbox (list): A list representing the bounding box in the format [xmin, ymin, xmax, ymax].

    Returns:
    bool: True if the bounding box is entirely inside the polygon, False otherwise.
    """
    xmin, ymin, xmax, ymax = bbox
    box_corners = [[xmin, ymin], [xmin, ymax], [xmax, ymin], [xmax, ymax]]

    for corner in box_corners:
        if point_in_polygon(corner, polygon):
            return True

    return False


def find_intervals(arr: list) -> List[int]:
    """
    Find intervals of consecutive occurrences of a specific value in a list.

    Parameters:
    - arr (list): A list of values.

    Returns:
    list: A list of intervals where the specified value occurs consecutively.
    Each interval is represented as a list [start, end].
    """
    intervals = []
    start = None

    for i, value in enumerate(arr):
        if value == 1:
            if start is None:
                start = i
        else:
            if start is not None:
                intervals.append([start, i - 1])
                start = None

    if start is not None:
        intervals.append([start, len(arr) - 1])

    return intervals


def convert_intervals_to_list(intervals: list, video_length: int) -> List:
    """
    Convert a list of intervals into a binary list representing time intervals.

    Parameters:
    - intervals (list): A list of intervals, each represented as [start, end].
    - video_length (int): The length of the video.

    Returns:
    list: A binary list where 1s indicate time intervals covered by the input intervals,
    and 0s indicate the rest of the time.
    """
    result_list = [0] * video_length

    for interval in intervals:
        start, end = interval
        start = max(0, start)
        end = min(video_length, end)
        for i in range(start, end + 1):
            result_list[i] = 1

    return result_list
