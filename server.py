from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    analyzed = emotion_detector(text_to_analyze)
    
    anger = analyzed['anger']
    disgust = analyzed['disgust']
    fear = analyzed['fear']
    joy = analyzed['joy']
    sadness = analyzed['sadness']
    dominant = analyzed['dominant_emotion']

    if dominant != None:
        return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant}."
    else:
        return "Invalid text! Please try again!"


@app.route("/")
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

