
from flask import Flask
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, EqualTo

#----------------------------------------------
#Database
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'retailbanking'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

app.run(debug=True)
#---------------------------------------------


class StatementDateForm(Form):
    
    start_date = DateField(' Start date', validators=[DataRequired()])
    end_date = DateField(' End date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StatementNumberForm(Form):
    
    number = IntegerField('number', validators=[DataRequired(), Length(min=1, max=30)])
    submit = SubmitField('Submit')

class TransferForm(Form):
    
    said = StringField(' scource Account Id', validators=[DataRequired()])
    taid = StringField(' target Account Id', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired(), Length(min=1, max=2)])
    submit = SubmitField('Submit')

class DepositForm(Form):
    
    aid = StringField('Account Id', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired(), Length(min=1, max=2)])
    submit = SubmitField('Submit')

class CreateAccountForm(Form):
    
    cid = StringField('Customer Id', validators=[DataRequired()])
    atype= StringField('Account type',validators=[DataRequired(), Length(min=2, max=20)])
    deposit = IntegerField('Deposit', validators=[DataRequired(), Length(min=1, max=2)])
    submit = SubmitField('Submit')

class RegistrationForm(Form):
    name = StringField('Customer Name',validators=[DataRequired(), Length(min=2, max=20)])
    ssnid = StringField('Customer SSN ID', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), Length(min=1, max=2)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')
    #reset = ResetField('Reset')


class LoginForm(Form):
    userId= StringField('UserId',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

import routes


