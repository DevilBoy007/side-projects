DESIGN:
	initially i was tempted to go with Express.js for the server, but eventually
settled with Flask due to the project's relatively simple requirements. Flask is not
a viable option for production products, but takes much less time to get working properly.
Since this is just an evaluation, i figured it was more important to emphasize my 
understanding of the process and less about technical, production level correctness. 

ASSUMPTIONS:

Flask assumes this file tree architecture:
```
	/project
	 |
	  - app.py
	  - templates
	  - static
```
where templates contain .html pages and static contains their respective stylesheets 
and resources

Modifying this architecture for our test, the structure should look like this:
```
/backend-dev-test
  |
  |- Dockerfile
  |- docker-compose.yml
  |- app.py
  |- templates
  |   |
  |   |- index.html
  |   |- login.html
  |   |_ register.html
  |
  |- static
  |- users.db
  |- requirements.txt
  |_ README.md
```
DATABASE:
 the following schema was used to create a sqlite database for our app to use:

	CREATE TABLE login(email varchar(64), password varchar(64));

to create a databse in your local directory, enter:
	sqlite3
into the terminal and you will enter an interactive sqlite shell. simply enter
the above command, and then save the database with the save command:

	.save users.db

and you should be good to go!
************************

	the biggest assumption that the API makes is that the incoming data will be base64
encoded. it makes this assumption to show decode functionality. in a real web 
request, the incoming parameters of the request would most likely be a JWT and should
be processed as such. 
	when submitting the data through a browser, since i didn't build out any web
scripting to encode the submission data, the decryption function will recognize that
the data isn't encrypted and will simply return the text data as it was received, which
is proper string format.
	when submitting data using cURL, we base64 encrypt the parameters
see the examples below for /login and /register endpoints. do this to see 
server properly decode and store strings in database

TESTING:

1. copy/paste the following command to build and start the app in your docker
   environment:

	docker-compose up

 - this will start up the REST server and allow you to stream the pings in your terminal
 - to start up the server in the background (so you can send curl requests
	without having to open a new terminal window/instance) enter this command instead:
	
	docker-compose up -d

Flask does not keep http connections alive by default and to change this setting you
would have to change a source file. we will not do that because we can test all
functionality without it.
the endpoints will respond to curl requests as individuals and not as a session,
even if you specify keep-alive in the headers

to get around this you can visit http://localhost:3000 and its associated endpoints
in a browser and your session will stay alive, allowing you to visualize the complete
setup

to verify the server responds, copy/paste the following command into your terminal

	curl localhost:3000

you should get a response 'You are not logged in'

#### cURL request endpoint tests ###

*********
/register

	curl -d "email=$(echo -n 'user@example.com' | base64)&password=$(echo -n '12345' | base64)" \
http://localhost:3000/register

--------------------------------
this will register an account if one does not exist, if you run this command a second
time, you will receive response from server that account already exists with that email

***************
/login

	curl -d "email=$(echo -n 'user@example.com' | base64)&password=$(echo -n '12345' | base64)" \
http://localhost:3000/login

--- server response will redirect to index page ---
	
	curl -d "email=$(echo -n 'user@example.com' | base64)&password=$(echo -n '54321' $
http://localhost:3000/login	

--- server response will be 'Invalid login combination' due to erroneous password ---

	curl -d "email=$(echo -n 'noUser@example.com' | base64)&password=$(echo -n '12345' $
http://localhost:3000/login

--- server response will be 'User does not exist' due to no matching email in database ---
--------------------------------

if user exists, server will add user's email to session and
redirect user to index page

*********
/logout

	curl localhost:3000/logout

------------------------------
this will return 'You cannot log out because you are not logged in' this is due to the
non-persistent connection. if you access this endpoint from the broswer tab that you
logged in from, it will properly return 'Logged out {yourEmail}'


ONCE YOU HAVE TESTED ENDPOINTS USING cURL:
	test them in the browser to test session functionality. the credentials
you created using the curl requests will allow you to login and visit the index page
as a logged in user, and will allow you to visit the /logout endpoint correctly

### browser endpoint tests ###

to observe api with session alive, enter the following in your browser URL:

	http://localhost:3000/
	http://localhost:3000/register
	http://localhost:3000/logout
	http://localhost:3000/login
	http://localhost:3000/logout

if you visit them in this order, provide data when prompted, and submit the forms, 
you will be able to see full functionality of the API
