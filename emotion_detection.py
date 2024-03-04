import requests

r = requests.get('https://www.python.org')
status_code = r.status_code
print(status_code)

def emotion_detector(text_to_analyze):
  
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  myobj = { "raw_document": { "text": text_to_analyze } }
  
  response = requests.post(url, json=myobj, headers=header)
  print(response.status_code)
  return response.text

emotion_detector('I like this game')