from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

#temp config
DATABASE = "fblog.db"
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '46n2w2K4sgxI'

app = Flask(__name__)

# pulls in config by looking for all caps
app.config.from_object(__name__)

# function used to connect to db, why not use the with statement?
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


@app.route("/", methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = "Invalid Credentials. Please try again."
		else:
			session['logged_in'] = True
			error = "no errors!!!"
			return redirect(url_for('main'))
	return render_template('login.html', error=error)


@app.route("/main")
def main():
	return render_template('main.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))

if __name__ == "__main__":
	app.run(debug=True)
