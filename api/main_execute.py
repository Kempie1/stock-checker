import requests
import json
import psycopg2
import psycopg2.extras
import json

from api_call_to_json import Api_call
from json_to_server import Json_to_server

class Execute:
    def execute_api_and_serve(self):
        Api = Api_call()
        Server = Json_to_server()

     
main = Execute()
main.execute_api_and_serve()

