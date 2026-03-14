"""server module"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """main function"""
    text_to_analyze = request.args.get('textToAnalyze')
    analyzed = emotion_detector(text_to_analyze)

    anger = analyzed['anger']
    disgust = analyzed['disgust']
    fear = analyzed['fear']
    joy = analyzed['joy']
    sadness = analyzed['sadness']
    dominant = analyzed['dominant_emotion']

    if dominant is not None:
        final_result = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} "
            f"and 'sadness': {sadness}. The dominant emotion is {dominant}."
        )
    else:
        final_result = "Invalid text! Please try again!"

    return final_result

@app.route("/")
def render_index_page():
    """rendering function"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
