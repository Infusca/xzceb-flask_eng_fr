""" language translator service """
import unittest
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(text):
    ''' translate english to french'''
    french_translation = language_translator.translate(text=text, model_id='en-fr').get_result()
    return french_translation.get('translations')[0].get('translation')

def frenchToEnglish(text):
    ''' translate french to english '''
    english_translation = language_translator.translate(text=text, model_id='fr-en').get_result()
    return english_translation.get('translations')[0].get('translation')

# french to english test cases
print(frenchToEnglish('Bonjour'))
print(frenchToEnglish('Je suis Nichola'))
print(frenchToEnglish('mon ami'))
print(frenchToEnglish('Au revoir'))
print(frenchToEnglish('bleu \n'))

# english to french test cases
print(englishToFrench('Hello world'))
print(englishToFrench('My name is Nichola'))
print(englishToFrench('I love cats and wolves.'))
print(englishToFrench('The Last Test Case'))
print(englishToFrench('Hello world'))


