import unittest, os, json
from user_data_pipeline.services.pipeline import import_files_to_export_format_json


GOOD_USER_LIST_DATA = [{'email': 'amitchell0@chronoengine.com',
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

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
good_data_path = os.path.join(THIS_DIR, 'data', 'good', 'small_input.csv')

class TestJSONExport(unittest.TestCase):
    def test_should_return_json_when_given_good_file(self):
        json_data, num = import_files_to_export_format_json((good_data_path, ))

        data = json.loads(json_data)

        self.assertEqual(data['user_list_size'], 3)
        self.assertListEqual(data['user_list'], GOOD_USER_LIST_DATA)


    def test_should_return_json_when_given_multiple_good_file(self):
        json_data, num = import_files_to_export_format_json((good_data_path, good_data_path))

        data = json.loads(json_data)

        self.assertEqual(data['user_list_size'], 6)
        self.assertListEqual(data['user_list'], GOOD_USER_LIST_DATA + GOOD_USER_LIST_DATA)
