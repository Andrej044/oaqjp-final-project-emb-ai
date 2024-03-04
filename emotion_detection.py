import requests
import json

def emotion_detector(text_to_analyze):
  
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  myobj = { "raw_document": { "text": text_to_analyze } }
  
  response = requests.post(url, json=myobj, headers=header)
  formatted_response = json.loads(response.text)
#   print(formatted_response)

  emotionPredictions = formatted_response['emotionPredictions'][0]
  anger = emotionPredictions['emotion']['anger']
  disgust = emotionPredictions['emotion']['disgust']
  fear = emotionPredictions['emotion']['fear']
  joy = emotionPredictions['emotion']['joy']
  sadness = emotionPredictions['emotion']['sadness']
#   print(anger)

  return response.text
