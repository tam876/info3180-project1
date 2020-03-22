from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class SignUpForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField('Gender',choices=[('Female','Female'), ('Male',"Male")])
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid email format")])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()], widget=TextArea())
    ppicture= FileField("Profile Picture", validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],'Images only')])