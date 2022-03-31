import base64
import sqlite3
import secrets
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
# generate a key to ensure integrity of requests and responses
app.secret_key = secrets.token_hex()
table = 'login'

def decode_base64(a):
    try:
        b = a.encode('ascii')
        c = base64.b64decode(b)
        return c.decode('ascii')
    except Exception as e:
        return a


def check_if_user_exists(email):
    try:
        # connect to user database
        db = sqlite3.connect('./users.db')
        cursor = db.cursor()
        statement = f"SELECT email FROM {table} WHERE email = ?" # create injection safe SQL statement
        cursor.execute(statement,(email,)) # transact databse
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result
    except Exception as e:
        raise e

def validate_credentials(email, password):
    try:
        # connect to database
        db = sqlite3.connect('./users.db')
        cursor = db.cursor()
        statement = f"SELECT password FROM {table} WHERE email = (?)"
        cursor.execute(statement, (email,))
        value = cursor.fetchone()[0]    # we store to variable so we can close the cursor/db connections
        cursor.close()
        db.close()
        return True if password == value else False
    except Exception as e:
        raise e


def add_user(email,password):
    try:
        # connect to user database
        db = sqlite3.connect('./users.db')
        statement = f"INSERT INTO {table} (email, password) VALUES (?,?)"
        db.execute(statement,(email,password))
        db.commit()
        db.close()
    except Exception as e:
        raise e


@app.route('/')
def index():
    print('you have a visitor!')
    if 'email' in session:   # we make this check at every endpoint that requires authentication
        return f"Logged in as {session['email']}" # production app would  render_template('index')
    return 'You are not logged in'

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = decode_base64(request.form['email'])
        password = decode_base64(request.form['password'])
        if check_if_user_exists(email) is None:
            add_user(email,password)
            session['email'] = email
            return redirect(url_for('index'))
        else: return 'This profile already exists'
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = decode_base64(request.form['email'])
        password = decode_base64(request.form['password'])
        if 'email' in session:
            return 'Already logged in'
        if (check_if_user_exists(email) is None):
            return 'User does not exist'
        else:
            if (validate_credentials(email, password)):
                print(f"adding {email} to session")
                session['email'] = email
                print(session['email'])
                return redirect(url_for('index'))
            else:
                return 'Invalid login combination!'
    return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index')) if session.pop('email', None) is not None else 'You cannot log out because you are not logged in'
    # try:
    #     print(f"logged out {session.pop('email')}")
    #     return(redirect(url_for('index')))
    # except Exception as e:
    #     return 'You cannot log out because you are not logged in'
