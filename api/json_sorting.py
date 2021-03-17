import json


with open('stock.json') as json_file:
    data = json.load(json_file)
    
      
    print(data['price']['regularMarketPrice'])
    print(data['price']['regularMarketPrice']['raw'])
    print(data['quoteType']['longName'])

    for price in data['price']:
        
        #print(price)
       # print(price)
        if price == 'currency':
            print(price)
  
        #print('Name: ' + p['name'])
        #print('Website: ' + p['website'])
        #print('From: ' + p['from'])
        #print('')

     