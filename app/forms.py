from flask.ext.wtf import Form
from wtforms import StringField, IntegerField,SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class AddTripForm(Form):
    trip_name= StringField('trip_name', validators=[DataRequired()])
    destination= StringField('destination', validators=[DataRequired()])
    
    friend= SelectField('friends', validators = [DataRequired()])


# class OrdersForm(Form):
# 	name_of_part = StringField('name of part', validators=[DataRequired()])
# 	manufacturer_of_part = StringField('manufacturer of part', validators=[DataRequired()])
	