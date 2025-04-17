# Soccer Analysis

**Soccer Analysis** is a computer vision project designed to analyze soccer match videos by employing advanced object detection, tracking algorithms, and camera movement compensation techniques. The project aims to extract insightful analytics, including player positioning, ball tracking, team assignments, and perspective transformations for comprehensive game analysis.

---

## Features

- **Object Detection**: Implements YOLOv5 for accurate detection of players and soccer balls within each video frame.
- **Object Tracking**: Uses robust tracking algorithms to maintain consistent object tracking across frames.
- **Camera Movement Estimation**: Calculates and compensates for camera movement to stabilize analytical data.
- **Team Assignment**: Classifies players into respective teams based on jersey color and other distinguishing visual features.
- **Player-Ball Association**: Determines player-ball interactions, identifying the player possessing or closest to the ball.
- **View Transformation**: Converts video footage from original view to a top-down perspective for strategic and spatial analysis.
- **Visualization**: Provides real-time visualizations of detections, tracking paths, and game analysis insights.

---

## Project Structure

```
Soccer_Analysis/
├── main.py
├── yolo_inference.py
├── camera_movement_estimator/
├── input_videos/
├── models/
├── player_ball_assigner/
├── runs/
│   └── detect/
│       └── predict/
├── stubs/
├── team_assigner/
├── trackers/
├── training/
├── utils/
└── view_transformer/
```

- **main.py**: Entry point for running the entire analysis pipeline.
- **yolo_inference.py**: Handles object detection logic using YOLOv5.
- **camera_movement_estimator/**: Modules for detecting and compensating camera movements.
- **player_ball_assigner/**: Logic for assigning the soccer ball to the nearest player.
- **team_assigner/**: Determines team membership of each player.
- **trackers/**: Contains tracking algorithms to follow objects frame by frame.
- **view_transformer/**: Converts original camera views into top-down field views for improved analysis.
- **utils/**: Helper functions and utilities supporting various modules.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PyTorch
- OpenCV
- NumPy

### Installation

1. Clone the repository:

```bash
git clone https://github.com/NishchalRavish/Soccer_Analysis.git
cd Soccer_Analysis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the analysis on a soccer match video:

```bash
python main.py --input_video path_to_video.mp4
```

Results will be stored in `runs/detect/predict/`.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgements

- [YOLOv5](https://github.com/ultralytics/yolov5) for object detection
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [PyTorch](https://pytorch.org/) as a deep learning framework

