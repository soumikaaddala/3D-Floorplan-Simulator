%%writefile app.py
from flask import Flask, request, jsonify, send_file
from utils import process_floorplan

app = Flask(__name__)

@app.route("/generate-3d", methods=["POST"])
def generate_3d():
    try:
        image_path = "floorplan.jpg"
        output_path = "output"
        output_file = process_floorplan(image_path, output_path)
        return send_file(output_file, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
