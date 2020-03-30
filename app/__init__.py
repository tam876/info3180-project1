from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://lmwfeawvhmyfzj:fea5bc945a59365737e2243e38fe098d70094bea9605fd77d6d81ad0d32374a8@ec2-3-234-109-123.compute-1.amazonaws.com:5432/dd9bpvuq2b1qb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']="./app/static/uploads"

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
