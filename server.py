''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, request

# Import the emotion_detector function from the package
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the Flask app
app = Flask("Emotion Detector")


#Flask deorator
@app.route("/emotionDetector")
def sent_dectector():
    """
    Route to analyze the emotional content of input text.

    Retrieves text from the query parameter 'textToAnalyze',
    passes it to the emotion_detector function, and returns
    a formatted string with emotion scores and dominant emotion.

    Returns:
       str: Formatted emotion analysis result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    print("TEXT:", text_to_analyze)

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    #for testing
    print("RESPONSE:", response)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return " Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    