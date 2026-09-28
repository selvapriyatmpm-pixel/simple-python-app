from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello RAJATHI! Welcome to my Python Web Application."
