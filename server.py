"""
Flask Web Server for Emotion Detection Application.
This module provides a web interface for analyzing emotions in text.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main page of the Emotion Detection application.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Analyze the provided text for emotions and return the result.

    Returns:
        JSON: Emotion analysis results or error message for invalid input.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    # Analyze emotion
    result = emotion_detector(text_to_analyze)

    # Handle error case (dominant_emotion is None)
    if result['dominant_emotion'] is None:
        return jsonify({
            'message': 'Invalid text! Please try again!'
        }), 400

    # Format successful response
    response = {
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
