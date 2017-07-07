from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mike:sekhmet1@localhost:3306/vintage'
db = SQLAlchemy(app)
db.create_all()