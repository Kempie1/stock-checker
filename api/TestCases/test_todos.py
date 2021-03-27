# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal, assert_true

# Local imports...
from services import get_todos
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

        todos = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]
        
        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
        response = get_todos()
        
        #mylist = ["apple", "banana", "cherry"]
       # mylist2 = ["apple", "banana", "cherr"]
       assert_list_equal(mylist,mylist2)


        

        r = json.dumps(response.json()).replace('null', '""')
        json.loads(r)
        
        # If the request is sent successfully, then I expect a response to be returned.
        print(r)

        if r == response2:
            print("True")
        else: 
            print("There are not the same")
       # assert_list_equal(response.json(), todos)

    def test_getting_todos_when_response_is_not_ok(self):
        # Configure the mock to not return a response with an OK status code.
        self.mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        response = get_todos()
        # If the response contains an error, I should get no todos.
        assert_is_none(response)


TestTodos = TestTodos()

TestTodos.setup_class()
TestTodos.teardown_class()
TestTodos.test_getting_todos_when_response_is_ok()


