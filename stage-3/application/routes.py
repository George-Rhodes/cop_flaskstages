from application import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
    return render_template('home.html', title='Home', posts=dummyData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

