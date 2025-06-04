# 3D-Floorplan-Simulator

# 🏠 2D to 3D Floor Plan Simulator using Flask and OpenCV

This project simulates a **3D visual effect from a 2D floor plan image** using Python, OpenCV, and Flask. It creates a lightweight and interactive web API where users can upload a floor plan and get back an enhanced version that looks 3D.

## ✨ Features

- Upload a 2D floor plan via an API endpoint.
- Simulates a 3D effect using perspective transform and shadow enhancement.
- Returns a downloadable `.png` image with the 3D appearance.
- Hosted using ngrok for public access in Google Colab.

## 📁 File Structure


## ⚙️ Requirements

Install these with pip:


Or using:

```bash
pip install -r requirements.txt

🚀 How to Run (in Google Colab or locally)
Upload your floorplan.jpg image.

Start Flask app with ngrok tunneling.

POST to /generate-3d endpoint.

Download and view FloorPlann_3D.png.

✅ Output Preview
Below is a sample output of a processed 2D floor plan made to look 3D:

![floorplan](https://github.com/user-attachments/assets/1597dbe1-e82f-4b16-80e7-63312424a7e0)
![image](https://github.com/user-attachments/assets/6d3de832-e277-434e-8406-063f784ad0a0)



