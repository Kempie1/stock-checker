# app.py
from flask import Flask, request, jsonify
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


#Returns a dictionary from the specified querry containing the column name and its value
def query_db(query, args=(), one=False):
    cursor = conn.cursor()
    cursor.execute(query, args)
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    cursor.close()
    return (r[0] if r else None) if one else r




@app.route('/getst/', methods=['GET'])
def getStock():
    print("Route getStock")
    ticker = request.args.get("ticker", None)
    print(ticker)
    response = {}
    if not ticker:
        response["ERROR"] = f"no ticker found, please send a ticker."
    elif len(ticker.split()) > 1:
        response["ERROR"] = f"more then one word, please send a ticker."
    elif len(ticker) > 10:
        response["ERROR"] = f"ticker symbol is too long."
    else:
        response = query_db(f"SELECT * FROM stock WHERE ticker_symbol='{ticker}';",one=True)
    if response == None:
        response={}
        response["ERROR"] = f"ticker not found in the Database, please try another ticker."
    return jsonify(response)


@app.route('/getavailable/', methods=['GET'])
def getAvailable():
    cursor = conn.cursor()
    print("Route getAvailable")
    response = {}
    cursor.execute("SELECT ticker_symbol FROM stock;")
    response["Stocks"] = cursor.fetchall()
    print(response)
    cursor.close()
    return jsonify(response)


@app.route('/')
def index():
    print("Index")
    return "<h1>Welcome to our server :)!!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)