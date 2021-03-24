# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
from nose.tools import assert_true
import requests

# Standard library imports...
from unittest.mock import Mock, patch

#Local Imports
from services import get_todos
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal


#Describition of the Test 
    # This will send a request and respond 
    #If the server repsonds with an okay respond then everything is fine 

def test_request_response():
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": "TSLA","region":"US"}
        headers = {
        'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        # Send a request to the API server and store the response.
        response = requests.get(url, headers=headers, params=querystring)
        # Confirm that the request-response cycle completed successfully.
        assert_true(response.ok)


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







test_request_response()
test_getting_todos()
test_getting_todos_when_response_is_ok()
test_getting_todos_when_response_is_not_ok()