from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps

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

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap 
	
@app.route("/procedure")
def proceed():
	return render_template('Flask_procedure.html')

@app.route("/proto")
def realestate():
	return render_template('realestate.html')

@app.route("/specs")
def specs():
	return render_template('presentation.html')

###Views
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
@login_required
def main():
	g.db = connect_db()
	cur = g.db.execute('select * from key_info_posts')
	posts = [dict(title=row[0], post=row[1], view=row[2]) for row in cur.fetchall()]
	g.db.close()
	return render_template('main.html', posts=posts)

@app.route("/add", methods=['POST'])
@login_required
def add():
	title = request.form['title']
	post = request.form['post']
	view = request.form['view']
	if not title or not post or not view:
		flash("All fields are required. Please try again.")
		return redirect(url_for('main'))
	else:
		g.db = connect_db()
		g.db.execute('insert into key_info_posts (title, posts, views) values (?,?,?)',
			[request.form['title'], request.form['post'], request.form['view']])
		g.db.commit()
		g.db.close()
		flash('New entry was successfully posted')
		return redirect(url_for('main'))


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))

#look at foundation 5 demo sheet		
@app.route("/test")
def testfoun():
	return render_template('foun5index.html')

#moved to run.py for heroku
#if __name__ == "__main__":
#	app.run(debug=False)
