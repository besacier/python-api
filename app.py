from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/filter", methods=["POST"])
def filter_data():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        content = json.load(file)
        data = content.get("data", [])
        filtered = [item for item in data if item.get("is_active") is True]
        return jsonify({"data": filtered})
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

