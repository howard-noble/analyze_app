# 🏉 Professional Rugby Match Analysis System

This is an open-source project dedicated to automating the analysis of rugby matches using computer vision.

The goal is to accept any video source (YouTube link or direct upload), analyze the footage frame-by-frame, and automatically identify, timestamp, and clip specific rugby moments from a list of over 60 defined events (e.g., 'Dominant Tackle', 'Scrum Wheel', 'Chip Kick').

## 🚧 Status: ML Pipeline is a Work-in-Progress

The current application structure is complete (Flask app, video download, OpenCV clipping, JSON output). However, the **event detection logic is currently a placeholder** that generates random timestamps for demonstration purposes.

**We are actively seeking contributors to build the Machine Learning and Heuristics pipeline!**

## ✨ Features (Complete)

* Input via YouTube URL or local video file upload.
* Video downloading via \pytube\ (for YouTube sources).
* Automatic clip extraction around detected moments using \OpenCV\.
* Web page output with **clickable timestamps**.
* Downloadable JSON metadata file.

## 🚀 Getting Started

### Prerequisites

You need Python 3.8+ and the following libraries:

\\\ash
pip install -r requirements.txt
\\\

### Running the Application

1.  Clone the repository:
    \\\ash
    git clone https://github.com/howard-noble/analyze_app.git
    cd analyze_app
    \\\
2.  Run the Flask app:
    \\\ash
    python app.py
    \\\
3.  Access the web interface at \http://0.0.0.0:5000/\.

## 🤝 Contributing

We need your help to develop the advanced detection logic. Please see the **[CONTRIBUTING.md](CONTRIBUTING.md)** file for guidelines on how to contribute.
