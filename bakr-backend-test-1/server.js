// import Express.js module and create the web application

const express = require('express')
const sqlite3 = require('sqlite3')
const app = express()
const port = 5000

app.get('/', function (req,res) {
	res.sendFile(__dirname + '/templates/index.html')
})
app.post('/', function (req,res) {
	switch (req.body) {
		case 'login':
		{
			res.redirect('/templates/login.html')
		}
		case 'register':
		{
			res.redirect('/templates/register.html')
		}
	}
})

/// define the endpoints and create function to handle the requests ///
app.get('/login', function (req,res) {
	res.sendFile(__dirname + '/templates/login.html')
})


app.use(express.static(__dirname + '/'))
app.listen(port, () => console.log('server is running'))
