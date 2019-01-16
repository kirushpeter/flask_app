
#we are importing the Flask class.

from flask import Flask

#we are creating an istance of the Flask class.
app = Flask(__name__)


#use the route() decorator to register the hello_world function for the /

@app.route('/hello_world')

def hello_world():
    return 'Hello World!'
