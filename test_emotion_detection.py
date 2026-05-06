from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #Test case for joy emotion result
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')
        
        #Test case for anger emotion result
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')
        
        #Test case for disgust emotion result
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust')
        
        #Test case for sadness emotion result
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')
        
        #Test case for fear emotion result
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()