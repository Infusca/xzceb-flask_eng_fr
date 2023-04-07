import unittest
import translator
from translator import french_to_english, english_to_french

# unit tests
class TestCases(unittest.TestCase):
    ''' test cases '''
    def test_french_to_english(self):
        ''' test french to english fxn '''
        actual = french_to_english(text='Bonjour')
        expected = 'Hello'
        self.assertEqual(actual, expected)
        self.assertIsNone(None)
        self.assertNotEqual(actual, 'unexpected')

    def test_english_to_french(self):
        ''' test english to french fxn '''
        actual = english_to_french(text='Hello world')
        expected = 'Bonjour le monde'
        self.assertEqual(actual, expected)
        self.assertIsNone(None)
        self.assertNotEqual(actual, 'unexpected')

if __name__ == '__main__':
    unittest.main()