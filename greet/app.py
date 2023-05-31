from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return '<h1>welcome</h1>'

@app.route('/welcome/home')
def say_welcome_home():
    return '<h1>welcome home</h1>'

@app.route('/welcome/back')
def say_welcome_back():
    return '<h1>welcome back</h1>'