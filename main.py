from flask import Flask, request, redirect, render_template
import string
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')



@app.route('/signup_form', methods=['POST'])
def display_signup_form():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']
    return username 
    username_error = ''
    password_error = ''
    confirm_email_error = ''
    email_error = ''
    return signup_form
    
    if not string.ascii(username):
        username_error = 'Not a valid character'
    else:
        username = str(username)
    if username < 3 or username > 20:
       username_error = 'Value out of range (3-20)' 
            
    if not string.ascii(password) :
        password_error = 'Not a valid character'
        password = ''
    else:
        password = str(password)
    if password < 3 or password > 20:
        password_error = 'Value out of range (3-20)'
        password = ''
    if not string.ascii(confirm_password):
        confirm_password_error = 'Not a valid character'
        confirm_password = ''
    else:
        confirm_password = str(confirm_password)
    if confirm_password < 3 or confirm_password > 20:
        confirm_password_error = 'Passwords must match'
        confirm_password = ''
    if not string.ascii(email):
        email_error = 'Not a valid character'
    else:
        email = str(email)
    if email < 3 or email > 20:
        email_error = 'Invalid email'

    if not username_error: 
        if not password_error:
            if not confirm_password_error:
                if not email_error:
                    return welcome_page.html

    else:
        return signup_form(username_error=username_error, password_error=password_error, confirm_password_error=confirm_password_error, email_error=email_error, username=username, password=password, confirm_password=confirm_password, email=email)
        
        

app.run()

