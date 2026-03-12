import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers=headers)
    formatted = json.loads(response.text)
    
    emotions = formatted['emotionPredictions'][0]['emotion']

    anger_score = float(emotions.get('anger', 0))
    disgust_score = float(emotions.get('disgust', 0))
    fear_score = float(emotions.get('fear', 0))
    joy_score = float(emotions.get('joy', 0))
    sadness_score = float(emotions.get('sadness', 0))

    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result