## Backend-Stock-Checker

Calling the Yahoo Finance API and sending the Data from that API to the SQL Database

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
Yahoo Finance Api.

In this format:

```.env
DB_HOST= Your Database Creditals GO HERE
DB_NAME= Your Database Creditals GO HERE
DB_USER= Your Database Creditals GO HERE
DB_PASS= Your Database Creditals GO HERE

APIKEY= Your API Creditals GO HERE
APIHOST= Your API Creditals GO HERE
```

At the Moment the Repository contains a mock and an Integration Test

Those Test can be executed by typing: 


```bash
$ pytest ORM
```

You can execute all python files in the ORM folder through this command

Execute the this file:

```bash
$ python ORM\main_execute.py
```

Follow the Instructions after that

## Contributing

This is a Private Repository. No changes allowed.

## SQL Commands

In the Database SQL foder is the SQL commands that were sued to create the Database. Those are just there as a reference. 

## ER Model of Database

This PNG file: ER Model of Database.png
Contains the ER Model of the Database

## Flask Server

Under the Folder Flask Server there is a  README.md file which will expplain the flask server

## License

[MIT](https://choosealicense.com/licenses/mit/)