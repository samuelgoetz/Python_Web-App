import unittest
from unittest.mock import patch
from flask import Flask
from app import hello  # Stelle sicher, dass `hello` korrekt importiert wird
 
class TestHelloFunction(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.add_url_rule('/hello', view_func=hello, methods=['POST'])
        self.client = self.app.test_client()
 
    @patch('app.render_template')
    @patch('app.redirect')
    def test_valid_input(self, mock_redirect, mock_render_template):
        # Mock-Objekte werden automatisch den Test-Argumenten übergeben
        # inputs = ["1 und 2", "2 und 1", "1,2", "2,1", "2&1", "1&2"]
        inputs = ["1 und 2", "2 und 1", "1,2", "2,1", "2&1", "1&2", "1 2", "12", "1/2"]
        for input_value in inputs:
            response = self.client.post('/hello', data={'name': input_value})
            mock_render_template.assert_called_once_with('hello.html', name=input_value)
            mock_redirect.assert_not_called()
            mock_render_template.reset_mock()
 
    
 
if __name__ == '__main__':
    unittest.main()