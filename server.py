from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze the emotion of supplied text."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid input! Please enter some text."

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid input! Please enter a valid text."

    return (
        f"anger: {result['anger']}<br>"
        f"disgust: {result['disgust']}<br>"
        f"fear: {result['fear']}<br>"
        f"joy: {result['joy']}<br>"
        f"sadness: {result['sadness']}<br>"
        f"<b>Dominant Emotion: {result['dominant_emotion']}</b>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
