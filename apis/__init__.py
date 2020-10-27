import json, os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mysqldb import MySQL

app = Flask(__name__)

with open(os.getcwd() + '/apis/db.json') as file:
    details = json.load(file)

app.config['SECRET_KEY'] = '5a8829076c843bf7474885f1a5d88c31'
app.config['MYSQL_HOST'] = details['host']
app.config['MYSQL_USER'] = details['user']
app.config['MYSQL_PASSWORD'] = details['password']
app.config['MYSQL_DB'] = details['db']
api = Api(app)
mysql = MySQL(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

from apis import views
