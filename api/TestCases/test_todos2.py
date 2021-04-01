from unittest.mock import Mock, patch
from nose.tools import assert_is_none, assert_list_equal, assert_true
import sys
sys.path.insert(1, '/Users/maximilianhues/Documents/CODE/stock-checker/api')
from services import get_todos, get_uncompleted_todos
import unittest

class TestUncompletedTodos(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.mock_get_todos_patcher = patch('services.get_todos')
        cls.mock_get_todos = cls.mock_get_todos_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_todos_patcher.stop()

    def test_getting_uncompleted_todos_when_todos_is_not_none(self):
        todo1 = {
            'symbol': 'TSLA'
        }
        todo2 = {
            'symbol': 'TSLA'
        }

        # Configure mock to return a response with a JSON-serialized list of todos.
        self.mock_get_todos.return_value = Mock()
        self.mock_get_todos.return_value.json.return_value = [todo1, todo2]
        
        # Call the service, which will get a list of todos filtered on completed.
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called.
        assert_true(self.mock_get_todos.called)

        print(uncompleted_todos)
        #print([todo1])
        # Confirm that the expected filtered list of todos was returned.
        assert_list_equal(uncompleted_todos, [todo1])

    def test_getting_uncompleted_todos_when_todos_is_none(self):
        # Configure mock to return None.
        self.mock_get_todos.return_value = None

        # Call the service, which will return an empty list.
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called.
        assert_true(self.mock_get_todos.called)

        # Confirm that an empty list was returned.
        assert_list_equal(uncompleted_todos, [])


#TestUncompletedTodos = TestUncompletedTodos()
#TestUncompletedTodos.setup_class()
#TestUncompletedTodos.test_getting_uncompleted_todos_when_todos_is_not_none()
#TestUncompletedTodos.test_getting_uncompleted_todos_when_todos_is_none()
#TestUncompletedTodos.teardown_class()