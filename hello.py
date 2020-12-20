from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return 'hello, post'
	return render_template('index.html')


@app.route('/service/')
def service():
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
	app.run(debug=True)
