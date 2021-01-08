from flask import Flask

# A Minimal App looks something like this:
app = Flask(__name__)
print(__name__)

# @app.route('/')
# def hello_world():
#    return 'Hello World!'