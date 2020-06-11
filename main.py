
import json
import requests
import unittest


class YaTranslatorTester(unittest.TestCase):

    def setUp(self):

        self.params = {
            'key': API_KEY,
            'text': 'привет',
            'lang': '{}-{}'.format('ru', 'en'),
        }

    def testing_translation(self):

        phrase_to_translate = requests.get(
            URL,
            params=self.params
        )
        response = phrase_to_translate.json()
        result = str(response['text'][0])
        self.assertEqual(result, 'hi')

    def testing_code_status(self):

        translating_source = requests.get(
            URL,
            params=self.params
        )
        response = translating_source.json()
        result = str(response['code'])
        self.assertEqual(result, '200')

class NegativeTester(unittest.TestCase):

    def setUp(self):
        
        self.params = {
            'key': API_KEY,
            'text': 'привет',
            'lang': '{}-{}'.format('ru', 'en'),
        }

    def testing_401_error(self):
        
        get_trnsl = requests.get(
            URL,
            params=self.params
        )
        response = get_trnsl.json()
        result = str(response['code'])
        self.assertEqual(result, '401')


if __name__ == '__main__':

  API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
  URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

  unittest.main()


