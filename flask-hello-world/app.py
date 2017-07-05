# Flask Hello World Application
# Based off RealPython Course
from flask import Flask

# create the flask application object
app = Flask(__name__)

# use decorator patterns to link view function to url paths
# then define the view using the a function returning a string
@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello World!"

# dynamic route based on url entered
@app.route("/test/<search_query>")
def search (search_query):
    return search_query

# dynamic route handlers of each kind
@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

if __name__ == "__main__":
	app.run()
