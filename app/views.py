from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Chris'} #fake user
	posts = [
		{
			'author': { 'nickname': 'John'},
			'body': 'Pretty day in SF!',
			'topic': 'weather'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'Movies cool',
			'topic': 'entertainment'
		},
	]
	return render_template('index.html',
		title = 'Home',
		user = user,
		posts = posts,)

