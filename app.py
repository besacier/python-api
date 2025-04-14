from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/filter", methods=["POST"])
def filter_data():
    try:
        content = request.get_json()  # ✅ accepts raw JSON
        data = content.get("data", [])
        filtered = [entry for entry in data if entry.get("is_active") is True]
        return jsonify({"data": filtered})
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)}), 400
