from flask import Flask, request, render_template, url_for, redirect, session, g
import os
from module_init import init_db, connect_db


DATABASE = 'db.sqlite3'
DEBUG = True
SECRET_KEY = os.urandom(24)
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)
init_db(app)


@app.before_request
def before_request():
	g.db = connect_db(app)


@app.teardown_request
def teardown_request():
	g.db.close()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/service/')
def service():
	g.db.execute()
	return render_template('service.html')


@app.route('/about/')
def about():
	return render_template('about.html')


@app.route('/contacts/')
def contacts():
	return render_template('contacts.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return redirect(url_for('add_service'))
	return render_template('login.html')


@app.route('/add_service/', methods=['GET', 'POST'])
def add_service():
	if request.method == 'POST':
		pass
	return render_template('add_service.html')


if __name__ == '__main__':
	app.run()
