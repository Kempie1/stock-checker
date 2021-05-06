import requests
import unittest

class test_Mock_Api(unittest.TestCase):
    
    def test_mock_api(self):
        response = requests.get('http://127.0.0.1:4000/json')
        response_body = response.json()
        print(response_body)
        assert response.status_code == 200
        assert response_body['get-statistics']['symbol'] == 'TSLA'

if __name__ == '__main__':
    unittest.main()