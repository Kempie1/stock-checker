# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
from nose.tools import assert_true, assert_is_not_none, assert_is_none, assert_list_equal
import requests
from unittest.mock import Mock, patch

#Local Imports
from services import get_todos, get_uncompleted_todos
from unittest.mock import Mock, patch
import os

#Describition of the Test 
    # This will send a request and respond 
    #If the server repsonds with an okay respond then everything is fine 


@patch('services.requests.get')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    #This is the fake responds 
    mock_get.return_value.ok = True 

    #This is the actual responds from the function get_todos
    # Call the service, which will send a request to the server.
    response = get_todos()
    #if the function does not return a response then the assert will go of / the real api does not anwser
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
    
 #@patch() works: You provide it a path to the function you want to mock. 
 #The function is found, patch() creates a Mock object, and the real function is temporarily replaced with the mock.
 #When get_todos() is called by the test, the function uses the mock_get the same way it would use the real get() method. 
 #That means that it calls mock_get like a function and expects it to return a response object.








@patch('services.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    # Configure the mock to return a response with an OK status code. Also, the mock should have
    # a `json()` method that returns a list of todos.
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_list_equal(response.json(), todos)


@patch('services.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    # Configure the mock to not return a response with an OK status code.
    mock_get.return_value.ok = False

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the response contains an error, I should get no todos.
    assert_is_none(response)






@patch('services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_not_none(mock_get_todos):       
    todo1 = {
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }
    todo2 = {
        'userId': 1,
        'id': 2,
        'title': 'Walk the dog',
        'completed': True
    }

    # Configure mock to return a response with a JSON-serialized list of todos.
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = [todo1, todo2]

    # Call the service, which will get a list of todos filtered on completed.
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert_true(mock_get_todos.called)

    # Confirm that the expected filtered list of todos was returned.
    assert_list_equal(uncompleted_todos, [todo1])


@patch('services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_none(mock_get_todos):
    # Configure mock to return None.
    mock_get_todos.return_value = None

    # Call the service, which will return an empty list.
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert_true(mock_get_todos.called)

    # Confirm that an empty list was returned.
    assert_list_equal(uncompleted_todos, [])

test_request_response()
test_getting_todos()
test_getting_todos_when_response_is_ok()
test_getting_todos_when_response_is_not_ok()
test_getting_uncompleted_todos_when_todos_is_not_none()
test_getting_uncompleted_todos_when_todos_is_none()