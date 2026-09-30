"""
Local fallback implementation of the Watson-style emotion detector.

The original course endpoint is not reachable from this computer, so this
version provides the same required output structure for local demonstration.
"""

def emotion_detector(text_to_analyze):
    """Detect five emotions and return the dominant emotion."""
    text = text_to_analyze.lower().strip()

    if not text:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    scores = {
        "anger": 0.05,
        "disgust": 0.05,
        "fear": 0.05,
        "joy": 0.05,
        "sadness": 0.05
    }

    keywords = {
        "anger": ["angry", "anger", "furious", "mad", "hate", "annoyed"],
        "disgust": ["disgusting", "disgust", "gross", "nasty", "awful"],
        "fear": ["afraid", "fear", "scared", "terrified", "worried"],
        "joy": ["happy", "glad", "joy", "excellent", "great", "love",
                "wonderful", "excited"],
        "sadness": ["sad", "unhappy", "cry", "depressed", "lonely",
                    "sorry"]
    }

    for emotion, words in keywords.items():
        for word in words:
            if word in text:
                scores[emotion] = 0.90
                break

    dominant_emotion = max(scores, key=scores.get)

    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion
    }
