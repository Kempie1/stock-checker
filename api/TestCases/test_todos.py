from unittest.mock import Mock, patch
from nose.tools import assert_is_none, assert_list_equal, assert_true
import sys
sys.path.insert(1, '/Users/maximilianhues/Documents/CODE/stock-checker/api')
from services import get_todos, get_uncompleted_todos
import unittest
import json

class TestTodos(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('services.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()
    
    def test_getting_todos_when_response_is_ok(self):
        # Configure the mock to return a response with an OK status code.
        self.mock_get.return_value.ok = True

        todos = {'symbol': 'TSLA'}

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
        response = get_todos()
        response_json = response.json()

        print(todos['symbol'])
        print(response_json['symbol'])
        print(response.json())

        if response_json['symbol'] == todos['symbol']:
            print("symbol is equal")
            
        if response.json() == todos:
            print("They are equal")
        else:
            print("They are not equal")

        self.maxDiff = None
        self.assertDictEqual(response.json(), todos)
        self.assertEqual(response_json['symbol'],todos['symbol'])

    def test_getting_todos_when_response_is_not_ok(self):
        # Configure the mock to not return a response with an OK status code.
        self.mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        response = get_todos()
        # If the response contains an error, I should get no todos.
        assert_is_none(response)

#TestTodos = TestTodos()
#TestTodos.setup_class()
#TestTodos.test_getting_todos_when_response_is_ok()
#TestTodos.teardown_class()