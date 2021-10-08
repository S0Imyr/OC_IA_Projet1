import os, uuid, argparse

import  requests

from extract_data import choose_random_line


LANGUAGES_3 = {'ara': "Arabic", "eng": "English", "fra": "French", "hin":"Hindi", "spa": "Spanish", "zho": "Madarin"}
LANGUAGES_2 = {'ar': "Arabic", "en": "English", "fr": "French", "hi":"Hindi", "sp": "Spanish", "zh": "Madarin"}
ABREVIATIONS_MATCH = {'ara': 'ar', 'eng': 'en', 'fra': 'fr', 'hin': 'hi', 'spa': 'es', 'zho': 'zh'}
DATA_URL_TEXTS = 'data/x_test.txt'
DATA_URL_LANGUAGES = 'data/y_test.txt'


class Translator:
    def __init__(self):
        self.subscription_key = str(os.environ.get("TRANSLATOR_TEXT_SUBSCRIPTION_KEY"))
        self.endpoint = str(os.environ.get("TRANSLATOR_TEXT_ENDPOINT"))
        self.location = str(os.environ.get("TRANSLATOR_TEXT_LOCATION"))


    def detect_language(self, text):
        path = '/detect'
        constructed_url = self.endpoint + path
        params = {
            'api-version': '3.0'
        }
        headers = {
        'Ocp-Apim-Subscription-Key': self.subscription_key,
        'Ocp-Apim-Subscription-Region': self.location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': str(text)
        }]
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        language = response[0]["language"]
        confidence = response[0]["score"]*100
        return language, confidence


def cli_detector(translator):
    parser = argparse.ArgumentParser(
        description='Detect the language of the text passed as an argument'
                    'If no argument is passed, a random line is choosen from the dataset.')
    parser.add_argument('-t', '--text',
                        help='Input line which we want to detect the language.')
    args = parser.parse_args()
    if args.text:
        text_informations = f"You choose to translate the text : \n" + args.text
        language_source = ""
        language_detected, confidence = translator.detect_language(args.text)
    else:
        random_text = choose_random_line(DATA_URL_TEXTS, DATA_URL_LANGUAGES)
        text_informations = "The random text is : \n" + random_text[1]
        language_source = random_text[0]                      
        language_detected, confidence = translator.detect_language(random_text)

    result = f"The detected language is {LANGUAGES_2[language_detected]} with a confidence of {confidence}%."
    print("\n", text_informations, "\n")
    print(result, "\n")
    if language_source:
        print(f'The language of the source text is {LANGUAGES_3[language_source]}')
        if language_detected == ABREVIATIONS_MATCH[language_source]:
            print("Success", "\n")
        else:
            print('Fail', "\n")
    else:
        print("The language source is unknown.", "\n")


if __name__=='__main__':
    cli_detector(Translator())
