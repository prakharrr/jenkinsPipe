from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
	return "running flask inside docker to run on a jenkins build file"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
