from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField)
from wtforms.validators import InputRequired, Length, Email

class StudentForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired(),
                                             Length(min=2, max=20)])
    lastname = StringField('Last Name',
                                validators=[InputRequired(),
                                    Length(min=2,max=30)])
    email = TextAreaField('Email Address', validators=[InputRequired(),
                                             Email()])
    age = IntegerField('Age', validators=[InputRequired()])
    active = BooleanField('Active Student', default='checked')
    bio = TextAreaField('Biography',
                            validators=[InputRequired(),
                                Length(max=200)])