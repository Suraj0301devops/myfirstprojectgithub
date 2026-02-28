
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Explicitly specify the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json.get("text", "")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return jsonify(summary)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
