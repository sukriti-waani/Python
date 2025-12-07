from flask import Flask

'''
It creates an instance of the Flask class, which will be our WSGI application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to Flask!!!!!!!"

@app.route("/index")
def index():
  return "This is the index page."

if __name__ == '__main__':
  app.run(debug=True)