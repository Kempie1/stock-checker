import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath

class Api_test():

    def api_request_test(self):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": "TSLA","region":"US"}
        headers = {
        'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            print(response)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

        #This is checking if the right input is coming in
        json_response = json.loads(response.text)
        pages = jsonpath.jsonpath(json_response, 'symbol')
        print(pages)
        assert pages == ['TSLA']

    def check_json(self):
         with open('stock.json') as json_file:
            try:
                self.data = json.load(json_file)
            except ValueError:
                print('Decoding JSON has failed')

Api_test = Api_test()
Api_test.api_request_test()

