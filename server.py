from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emo_detector():
  text_to_analyze = request.args.get('textToAnalyze')
  response = emo_detector(text_to_analyze)
  return response

@app.route('/')
def render_index_page():
  return render_template('index.html')

