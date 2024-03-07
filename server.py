"""Import Flask and EmotionDetection module."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emo_detector():
    """render domination emotion when user use emotionDetector route"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    domination_emotion = response['domination_emotion']
    if domination_emotion is None:
        return 'Invalid text! Please try again!.'
    return (
        f'For the given statement, the system response is "anger": {response["anger"]},' 
        f'"disgust": {response["disgust"]},' 
        f'"fear": {response["fear"]},'
        f'"joy": {response["joy"]}'
        f' and "sadness": {response["sadness"]}.' 
        f'The dominant emotion is {response["domination_emotion"]}.')

@app.route('/')
def render_index_page():
    """render main static page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
