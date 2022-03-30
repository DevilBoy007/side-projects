# Using flask to make an api
# import necessary libraries and functions
import cgi, cgitb
import sqlite3
from flask import Flask, render_template, escape, request, redirect, jsonify

cgitb.enable()

# creating a Flask app
app = Flask(__name__)


# THIS FUNCTION NEEDS TO CHECK CASE WHERE NAME EXISTS IN DATABASE
def create_user(email, password):
# create injection safe variables to use in our statements
    email_: string = '{}'.format(email)
    password_ = '{}'.format(password)
# connect to user database
    db = sqlite3.connect('./users.db')
    #
    #	this is where we need to check if name exists in database (uid [pk]) ?
    #

    # add all of the info from the form into the database in their respective fields
    add = "INSERT INTO login (email, password) VALUES ('%s','%s');" % (email_, password_)
    db.execute(add) # execute the statement

    # save the changes and close the connection to user database
    db.commit()
    db.close()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template('index.html')
    if(request.method == 'POST'):
        if(request.body['action'] == 'login'):
            return redirect('login.html', code = 302)
        else if (request.body['action'] == 'register'):
            return redirect('register.html', code = 302)
        else:
            return redirect('pagenotfound.html',code=404)

@app.route('/login.html')

@app.route('/register.html', methods = ['GET','POST'])
def register():
    error = None
    if(request.method =='POST'):
        create_user(request.body['email'],request.body['password'])
    return render_template('index.html')



# driver function
if __name__ == '__main__':
    app.run(debug = True)
