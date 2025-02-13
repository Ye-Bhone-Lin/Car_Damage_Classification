## Car_Damage_Classification

### 🚀 Overview
This project focuses on car damage classification using YOLO (You Only Look Once), a deep learning model for object detection. The model detects and classifies car damages such as dents, glass shatter, lamp broken, and scratches from images.

Image Upload: Users can upload car images for analysis.

Damage Detection: Uses a trained YOLO model (best.pt) to detect and classify damages.

Confidence Score: Displays confidence percentages for each detected damage type.

Interactive UI: Built with Streamlit for easy user interaction.

### 🏎️ How It WorksUpload a car image using the Streamlit UI.
YOLO model processes the image and detects damages.

Detection results are displayed with bounding boxes.

Classification messages indicate damage severity:

🔴 Strong Confidence (>50%)

🟡 Possible Damage (10-50%)

🟢 No Damage (<10%)

### Model DetailsArchitecture: YOLO-based object detection
Classes:

0 - Dent

1 - Glass Shatter

2 - Lamp Broken

3 - Scratch

Here is the demonstration: https://b6kont4ojpe5zpyqy8mgcf.streamlit.app/

![image](https://github.com/user-attachments/assets/c544ecf3-3207-4d40-bb40-ff15f9fb34d6)

