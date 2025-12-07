# Import Flask class to create the web app
# render_template is used to load HTML files
# request is used to read data sent by the user (forms, POST requests)
from flask import Flask, render_template, request

'''
This creates an instance of the Flask class.
This object (app) will act as the WSGI application
that handles incoming web requests.
'''
### WSGI Application
app = Flask(__name__)

# This route runs when the user visits the home page "/"
@app.route("/")
def welcome():
  # Returns simple HTML directly as a response
  return "<html><H1>Welcome to Flask!</H1></html>"

# This route runs when the user visits "/index"
# Only GET requests are allowed
@app.route("/index", methods=['GET'])
def index():
  # Renders (loads) index.html from the templates folder
  return render_template("index.html")

# This route runs when the user visits "/about"
@app.route("/about")
def about():
  # Renders (loads) about.html from the templates folder
  return render_template("about.html")

# This route handles both GET and POST requests
# GET → shows the form
# POST → receives the form data
@app.route('/form', methods=['GET', 'POST'])
def form():
  # Check if the form was submitted (POST request)
  if request.method == 'POST':
    # Get the value entered in the input field named "name"
    name = request.form['name']
    
    # Return a greeting using the submitted name
    return f'Hello, {name}!'
  
  # If request is GET, show the form.html page
  return render_template('form.html')

# This ensures the app runs only when this file is executed directly
if __name__ == '__main__':
  # Starts the Flask development server
  # debug=True shows errors in the browser and auto-reloads the server
  app.run(debug=True)
