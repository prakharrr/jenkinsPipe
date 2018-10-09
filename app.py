from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
	return "What what what?"


if __name__ == "__main__":
    app.run(debug=True,host='localhost')
