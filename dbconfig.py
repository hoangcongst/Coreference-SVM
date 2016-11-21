from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'nlp'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.1'

mysql.init_app(app)
connection = mysql.connect();
cursor = connection.cursor()