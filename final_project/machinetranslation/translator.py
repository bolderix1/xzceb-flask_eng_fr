'''
transaltor
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

'''
translate E2F
'''
def english_to_french(english_text):
    #write the code here
    language_translator = english_text
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    return french_text
'''
translate E2F
'''
def french_to_english(french_text):
    #write the code here
    language_translator = french_text
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    return english_text
