from flask import Flask 

app = Flask(__name__)

@app.route("/")
def unnamed():
	print("nothing to see here")
@app.route("/hello")

if __name__ == "__main__":
	app.run()

