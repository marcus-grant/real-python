# Import the Flask class from flask package
from flask import Flask

# create the app object
app = Flask(__name__)

# use decorator to link view function to url
@app.route("/")
@app.route("/hello")

# define the view using a function, returning a str
def hello_world():
    return "Hello World!"

# start the development server using run() method
if __name__ == "__main__":
    app.run()
