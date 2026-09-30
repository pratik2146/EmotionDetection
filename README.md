# Emotion Detection Application

## Project Description

An Emotion Detection web application that analyzes text and identifies
anger, disgust, fear, joy, sadness, and the dominant emotion.

## Note

The original course Watson NLP endpoint was not reachable from the local
computer during development. This local demonstration therefore provides
the same required function and output structure without requiring the
remote endpoint.

## Technologies

- Python
- Flask
- Requests
- HTML/CSS/JavaScript
- Unit Testing
- Pylint

## Run

```bash
pip install -r requirements.txt
python -m unittest test_emotion_detection.py
python server.py
```

Open:

http://127.0.0.1:5000

## Example Inputs

- I am very happy today
- I am very angry
- This is disgusting
- I am afraid
- I am very sad
