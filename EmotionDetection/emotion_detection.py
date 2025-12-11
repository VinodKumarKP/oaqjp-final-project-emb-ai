import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Define the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Construct the input JSON payload
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send the POST request to the API
    response = requests.post(url, json=myobj, headers=headers)

    # Convert the response text to a Python dictionary
    formatted_response = json.loads(response.text)

    # Check if the response contains the expected keys (Status Code 200)
    if response.status_code == 200:
        # Extract the dictionary containing emotion scores
        # Note: The API returns a list 'emotionPredictions', we take the first element
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Extract specific scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        # Determine the dominant emotion (the key with the highest value)
        dominant_emotion = max(emotions, key=emotions.get)

        # Return the formatted dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    # If the server returns an error (e.g., status 400 or 500), return the raw response
    else:
        return formatted_response