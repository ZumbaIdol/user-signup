from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup_form', methods=['POST'])
def display_signup_form():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    confirm_password_error = ''
    confirm_email_error = ''
    email_error = ''
    
    if username == "" or len(username) < 3 or len(username) > 20:
       username_error = 'Value out of range (3-20)' 
            
    if password == "" or len(password) < 3 or len(password) > 20:
        password_error = 'Value out of range (3-20)'
        password = ''
    
    if confirm_password == "" or len(confirm_password) < 3 or len(confirm_password) > 20:
        confirm_password_error = 'Passwords must match'
        confirm_password = ''
    
    if email != "":
        if "@" or "." not in email:
            email_error = 'Invalid entry'
        
        if len(email) < 3 or len(email) > 20:
            email_error = 'Invalid email'

    if username_error == "" and password_error == "" and confirm_password_error == "" and email_error == "": 
                            
        return render_template('welcome_page.html', username=username)

    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error, confirm_password_error=confirm_password_error, email_error=email_error)
        
@app.route("/")
def index():
    return render_template('signup_form.html')
       

app.run()

