from flask import Flask

app = Flask(__name__)


# routing to the root directory
@app.route("/")
def index():
    return "Hello World"


# routing using a variable
@app.route("/user/<username>")
def name(username):
    return "Hello World " + username


# app = if __name__ == "__main__":#     pass

if __name__ == "__main__":
    app.run(debug=True)
