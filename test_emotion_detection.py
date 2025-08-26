"""
Unit Tests for Emotion Detection functionality.
This module tests the emotion detection with various input texts.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for the emotion detection functionality.
    """

    def test_emotion_detector_joy(self):
        """
        Test that the emotion detector correctly identifies joy.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        """
        Test that the emotion detector correctly identifies anger.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """
        Test that the emotion detector correctly identifies disgust.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_sadness(self):
        """
        Test that the emotion detector correctly identifies sadness.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        """
        Test that the emotion detector correctly identifies fear.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()