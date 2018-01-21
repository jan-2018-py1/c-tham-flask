from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'flaskRegistrationValidation'

import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
PASSWORD_REGEX = re.compile(r'^[A-Z].*\d|\d.*[A-Z]') 
DOB_REGEX = re.compile(r'19|20[0-9]{2}-[0-9]{2}-[0-9]{2}')
# A-Z, any char with 0 or more, digit  or  digit, any char with 0 or more, A-Z

from datetime import datetime

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/',methods=['POST'])
def process():
  print "** Got Post Info **"
  error = False
  today = str(datetime.now())[:10]
  print 'today is '+today
  email = request.form['email']
  firstname = request.form['firstname']
  lastname = request.form['lastname']
  password1 = request.form['password1']
  password2 = request.form['password2']
  dob = request.form['dob']
  print '* ',email, firstname, lastname, password1, password2, dob
#email
  if len(email) < 1:
    flash('** Your Email cannot be empty! **','error_empty')
    error = True
  elif not EMAIL_REGEX.match(email):
    flash("** Invalid Email Address! **",'error_invalid')
    error = True
#first name
  if len(firstname) < 1:
    flash('** Your First Name cannot be empty! **','error_empty')
    error = True
  elif not NAME_REGEX.match(firstname):
    flash('** Your First Name cannot contain any numbers! **',"error_invalid")
    error = True
#last name
  if len(lastname) < 1:
    flash('** Your Last Name cannot be empty! **','error_empty')
    error = True
  elif not NAME_REGEX.match(lastname):
    flash('** Your Last Name cannot contain any numbers! **',"error_invalid")
    error = True
#password
  if len(password1) < 1:
    flash('** Your Password cannot be empty! **','error_empty')
    error = True 
  elif len(password1) < 8:
    flash('** Your Password shoud be more than 8 characters **','error_invalid')
    error = True
  elif not PASSWORD_REGEX.match(password1):
    flash('** A password to have at least 1 uppercase letter and 1 numeric value **','error_ninja')
    error = True
#confirm password
  if len(password2) < 1:
    flash('** A confirm password cannot be empty! **','error_empty')
    error = True
  elif len(password2) < 8:
    flash('** Your confirm password shoud be more than 8 characters **','error_invalid')
    error = True
  elif not PASSWORD_REGEX.match(password2):
    flash('** A confirm password to have at least 1 uppercase letter and 1 numeric value **','error_ninja')
    error = True
#match password
  if password1 != password2:
    flash('** Password and password confirmation should match! **','error_invalid')
    error = True
#date of birth
  if len(dob) < 1:
    flash('** Your date of birth cannot be empty! **','error_hacker')
    error = True
  elif not DOB_REGEX.match(dob):
    flash('** Your date of birth is invalid! **','error_hacker')
    error = True
  elif str(dob) > today:
    flash('** Your date of birth must be from the past! **','error_hacker')
    error = True
#others
  if error == False:
    flash('Thanks for submitting your information.','pass')
    flash(str('('+email+') ('+firstname+') ('+lastname+') ('+password1+')  ('+password2+') ('+dob+')'),'pass')
  return redirect('/')

app.run(debug=True)
