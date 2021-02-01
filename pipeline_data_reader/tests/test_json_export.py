import unittest, os, json
from pipeline_data_reader.services.pipeline_data_reader import import_files_to_export_format_json


GOOD_DATA = [{'email': 'amitchell0@chronoengine.com',
   'first name': 'Ashley',
   'last name': 'Mitchell',
   'list_id': 1},
  {'email': 'lstanley1@netvibes.com',
   'first name': 'Lois',
   'last name': 'Stanley',
   'list_id': 2},
  {'email': 'sbrown2@google.es',
   'first name': 'Sean',
   'last name': 'Brown',
   'list_id': 3}]

class TestJSONExport(unittest.TestCase):
    def test_should_return_json_when_given_good_file(self):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        json_data, num = import_files_to_export_format_json((os.path.join(THIS_DIR, 'data/good/small_input.csv'), ))

        data = json.loads(json_data)

        self.assertEqual(data['user_list_size'], 3)

        self.assertListEqual(data['user_list'], GOOD_DATA)


    def test_should_return_json_when_given_multiple_good_file(self):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        json_data, num = import_files_to_export_format_json((
            os.path.join(THIS_DIR, 'data/good/small_input.csv'), 
            os.path.join(THIS_DIR, 'data/good/small_input.csv')))

        data = json.loads(json_data)

        self.assertEqual(data['user_list_size'], 6)