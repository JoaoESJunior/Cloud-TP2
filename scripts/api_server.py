
from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

model_path = "/home/joaojunior/project2-pv2/model.pickle"

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.json
    songs = data.get("songs", [])
    model = pd.read_pickle(model_path)

    recommendations = []
    for rule in model:
        if set(rule[0]).issubset(set(songs)):
            recommendations.extend(rule[1])

    return jsonify({
        "model_date": os.path.getmtime(model_path),
        "songs": list(set(recommendations)),
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
