# 🏉 Professional Rugby Match Analysis System

This is an open-source project dedicated to automating the analysis of rugby matches using computer vision.

The goal is to accept any video source and automatically identify, timestamp, and clip specific rugby moments from a list of over 60 defined events.

## 🚧 Status: ML Pipeline is a Work-in-Progress

The current application structure (Flask app, video download, clipping) is complete. However, the **event detection logic is currently a placeholder** that generates random timestamps.

**We are actively seeking contributors to build the Machine Learning and Heuristics pipeline!**

## ✨ Features (Complete)

* Input via YouTube URL or local video file upload.
* Video downloading via \pytube\.
* Automatic clip extraction around detected moments using \OpenCV\.
* Web page output with **clickable timestamps**.
* Downloadable JSON metadata file.

## 🚀 Getting Started

### Prerequisites

You need Python 3.8+ and the dependencies listed in \equirements.txt\.

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

## 🤝 Contributing

See the **[CONTRIBUTING.md](CONTRIBUTING.md)** file for guidelines on how to contribute to the Machine Learning model and heuristics logic.
