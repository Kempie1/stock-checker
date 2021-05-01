import mock
import unittest
import requests
from requests.exceptions import HTTPError
from services import real_api_request

class Mock(unittest.TestCase):

    @mock.patch('requests.get')
    def mock_api(self, mock_get):
        #Arrange
        mock_response = mock.Mock()
        mock_response.status_code = 200
   
        mock_response.json = mock.Mock(
            return_value={'symbol': 'TSLA'}
        )
        
        mock_get.return_value = mock_response
        #Act
        response = real_api_request()
        #Assert
        self.assertEqual(response, mock_response)

mock_api = Mock()
mock_api.mock_api()

