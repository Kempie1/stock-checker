## Backend-Stock-Checker

Calling the Yahoo Finance API and sending the Data from that API to the SQL Database using SQLAlchemy ORM and psycopg2 

## Installation

Install the required Packages by typing:

```bash
$ pip install -r requirements.txt
```

## Usage 

Type in your user creditails into the .env file

Go to the git cloned directory with cd and ls and 
past the command into your Terminal

```bash
$ touch .env 
```

After that insert you Creditails for the Database and
Yahoo Finance Api. Including your system path example below.

In this format:

```.env
Path to ORM and ORMLogic files example:

APIFOLDER = "/Users/maximilianhues/Documents/CODE/stock-checker/api"
ORMLogic = "/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM/ORMLogic"
ORM = "/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM"
TestCases = "/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM/TestCases"
TestJson = "/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM/TestCases/teststock.json"
MockFolder = "/Users/maximilianhues/Documents/CODE/stock-checker/api/Mocks"

DB_URL= "Your Database URL Creditals GO HERE"

APIKEY= "Your API Creditals GO HERE"
APIHOST= "Your API Creditals GO HERE"
```

CODE Profesors our Api and Database are hosted on HEROKU you can get your creditals at HEROKU:

Link: Click [here](heroku.com) to go to heroku
```
You have been invited via your e-mail (approx. May 3)

To get your database creditals you would have to go to stockcheckerdb under installed add-ons click on Heroku-Postgres then click on settings and 'View Credentials..."
```

At the Moment the Repository contains a mock and an Integration Test

Those Test can be executed by typing: 

```bash
$ pytest ORM
```

To initlaize the database run 

```bash
$ python ORM/ORMLogic/declarative.py
```

You can execute all python files in the ORM folder through this command

Execute the this file:

```bash
$ python ORM\main_execute.py
```

## Contributing

This is a Private Repository. No changes allowed.

## SQL Commands

In the Database SQL foder is the SQL commands that were sued to create the Database. Those are just there as a reference. 

## ER Model of Database

This PNG file: ER Model of Database.png
Contains the ER Model of the Database

# Flask Server

querries and returns the given stock row as a json.
Currently hosted on Heroku

## Installation

Use the package manager pip to install get the requirenments from requirements.txt in the previous folder.

## Usage
```
https://stockcheckerdb.herokuapp.com/getavailable/

https://stockcheckerdb.herokuapp.com/getst/?ticker=AAPL
```
or if ran localy
```
localhost:{THE Port}/getst/?ticker=AAPL
```
for the json file of the ticker AAPL.


## License

[MIT](https://choosealicense.com/licenses/mit/)