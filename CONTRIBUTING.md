# 🏉 Contributing to the Rugby Match Analysis System

Thank you for your interest in contributing! This project aims to create an open-source tool capable of automatically identifying and clipping over 60 specific rugby moments from any video source.

Our primary focus is moving from a placeholder (random) detection system to a robust Machine Learning and Heuristics pipeline.

## 🌟 Areas for Contribution

We need expertise in three main areas to achieve our goal:

### 1. The Machine Learning Model (Computer Vision)
The core challenge is training a model capable of recognizing low-level player states, object interaction, and field position across frames, likely using frameworks like YOLOv8.

### 2. The Heuristics and Event Logic (Python)
Writing Python functions (to replace the placeholder logic in \un_analysis_pipeline\) that convert raw ML output into definitive high-level \RUGBY_EVENTS\ moments.

### 3. Data Collection and Annotation
Identifying publicly available rugby footage and/or assisting with the annotation (labeling bounding boxes) of actions and objects in video clips.

## 💡 How to Submit a Contribution

1.  **Fork the Repository:** Create a fork of the main repository.
2.  **Create a New Branch:** Base your work on the \master\ branch and create a descriptive branch.
3.  **Open a Pull Request (PR):** Open a Pull Request against the \master\ branch of the main repository. Please describe the changes in detail.

## 🐛 Reporting Bugs

Please open an **Issue** on GitHub with a clear title, steps to reproduce the error, and the expected vs. actual behavior.
