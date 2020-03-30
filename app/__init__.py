from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://yrymkwjahdzqbu:927e1d87bfb0d7bc021e4f2b5a6bf497f07faa76b5048fa02dab447813872232@ec2-54-197-48-79.compute-1.amazonaws.com:5432/dffrh5bmmdgr39"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']="./app/static/uploads"

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
