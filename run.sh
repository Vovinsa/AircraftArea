#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Provide VIDEO_PATH, POLYGON_PATH, OUTPUT_PATH"
  exit 1
fi

video_path=$1
polygon_path=$2
output_path=$3

echo "Creating virtual environment..."
python3 -m venv venv
pip3 install -U pip
source venv2/bin/activate

echo "Installing requirements..."
pip3 install -r requirements.txt

echo "Running inference..."
python3 main.py --output-path "$output_path" --video-path "$video_path" --polygon-path "$polygon_path"

echo "Done"