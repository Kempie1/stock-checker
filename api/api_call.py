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
file1.write(response_string)
file1.close()

f1=open("stock.json","r+")
input=f1.read()
print(input) #This still has a comma
#input=input.replace('{','\n {')
print(input) #This one does not have a comma anymore
f2=open("stock.json","w+")
f2.write(input)
f1.close()
f2.close()

