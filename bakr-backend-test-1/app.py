import base64
import sqlite3
import secrets
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
# generate a key to ensure integrity of requests and responses
app.secret_key = secrets.token_hex()
print(app.secret_key)   # comment out before submission !!!!
table = 'login'

def check_if_user_exists(email):
    # connect to user database
    db = sqlite3.connect('./users.db')
    cursor = db.cursor()
    fetch = f"SELECT email FROM {table} WHERE email = ?"
    cursor.execute(fetch,(email,))
    result = cursor.fetchone()
    return result

def add_user(email,password):
    # connect to user database
    db = sqlite3.connect('./users.db')
    add = f"INSERT INTO {table} (email, password) VALUES (?,?)"
    db.execute(add,(email,password))
    db.commit()
    db.close()

@app.route('/')
def index():
    print('you have a visitor!')
    if 'email' in session:   # we make this check at every endpoint that requires authentication
        return f"Logged in as {session['email']}" # production app would  render_template('index')
    return 'You are not logged in'

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if check_if_user_exists(email) is None:
            add_user(email,password)
            session['email'] = email
            return redirect(url_for('index'))
        else: return 'This profile already exists'
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"/*** login request from {email} ***\\")
        if (check_if_user_exists(email) is None):
            return 'User does not exist'
        else:
            #if (validate_credentials(request.form['email'],request.form['password'])):
            session['email'] = email
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return(redirect(url_for('index')))
