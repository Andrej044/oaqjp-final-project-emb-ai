import requests
import json

def emotion_detector(text_to_analyze):
  
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  myobj = { "raw_document": { "text": text_to_analyze } }
  
  emotion_dictionary = {
    'anger' : None,
    'disgust' : None,
    'fear' : None,
    'joy' : None,
    'sadness' : None,
    'domination_emotion' : None
  }

  
  def find_domination_emotion(arr):
    arr.sort(reverse=True)
    emotion_name = None
    
    for emotion in emotion_dictionary:
      if arr[0] == emotion_dictionary[emotion]:
        emotion_name = emotion
        return emotion_name
    return emotion_name 
  
  response = requests.post(url, json=myobj, headers=header)
  formatted_response = json.loads(response.text)
  
  if response.status_code == 200:
    emotionPredictions = formatted_response['emotionPredictions'][0]
    anger_score = emotionPredictions['emotion']['anger']
    disgust_score = emotionPredictions['emotion']['disgust']
    fear_score = emotionPredictions['emotion']['fear']
    joy_score = emotionPredictions['emotion']['joy']
    sadness_score = emotionPredictions['emotion']['sadness']
    
    emotion_dictionary = {
    'anger' : anger_score,
    'disgust' : disgust_score,
    'fear' : fear_score,
    'joy' : joy_score,
    'sadness' : sadness_score,
    'domination_emotion' : None
    }
    
    emotion_array = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    domination_emotion = find_domination_emotion(emotion_array)
    
    emotion_dictionary.update({'domination_emotion': domination_emotion})
    return emotion_dictionary
  elif response.status_code == 400:
    return emotion_dictionary
