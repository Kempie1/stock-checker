import requests
import json

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"

querystring = {"symbol":"AAPL","region":"US"}

headers = {
    'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

response_string = response.text

file1 = open("stock.json","w") 
#f1=open("stock.json","r+")
#f2=open("stock.json","w+")
file1.write(response_string)

#input = f2.read()
#input=input.replace('{','\n {')
#f2.write(input)
file1.close()

#f2.close()

