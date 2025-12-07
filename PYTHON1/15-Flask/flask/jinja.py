# Building Url dynamically
# Variable rule
# Jinja 2 Template Engine
'''
{{ }} -> Used to print variables in HTML (Jinja expression)
{% %} -> Used for control statements like for, if in templates
{# #} -> Used for comments in Jinja templates
'''

# Import Flask and useful helpers
from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app object
app = Flask(__name__)

# Route for home page "/"
@app.route("/")
def welcome():
  # Send simple HTML text as response
  return "<html><H1>Welcome to Flask!</H1></html>"

# Route for "/index" page (only GET requests)
@app.route("/index", methods=['GET'])
def index():
  # Render index.html from templates folder
  return render_template("index.html")

# Route for "/about" page
@app.route("/about")
def about():
  # Render about.html from templates folder
  return render_template("about.html")


# Route with variable rule: score must be int in URL
@app.route('/success/<int:score>')
def success(score):
  # Initialize result string
  res = ""
  # Check pass / fail based on score
  if score >= 50:
    res = "Passed!"
  else:
    res = "Failed!"
  # Send result to result.html template
  return render_template('result.html', result=res)

# Route with variable rule: score must be int in URL
@app.route('/successres/<int:score>')
def successres(score):
  # Initialize result string
  res = ""
  # Check pass / fail based on score
  if score >= 50:
    res = "Passed!"
  else:
    res = "Failed!"

  # Create a dictionary to hold data for template
  exp = {'score': score, 'result': res}

  # Pass dictionary 'exp' to result1.html as 'result'
  return render_template('result1.html', result=exp)


# Route to show result using if condition inside template
@app.route('/successif/<int:score>')
def successif(score):
  # Pass score directly to result.html
  return render_template('result.html', result=score)

# Another route to show fail page (also uses result.html)
@app.route('/fail/<int:score>')
def fail(score):
  # Pass score directly to result.html
  return render_template('result.html', result=score)

# Route to handle form page and form submission
@app.route('/submit', methods=['GET', 'POST'])
def submit1():
  # If method is GET → just show the form page
  if request.method == 'GET':
    # Load getresults.html (the form page)
    return render_template('getresults.html')

  # If method is POST → read form data and process it
  science = float(request.form['science'])
  maths = float(request.form['maths'])
  c = float(request.form['c'])
  data_science = float(request.form['datascience'])

  # Calculate average of 4 subjects
  total_score = (science + maths + c + data_science) / 4

  # Redirect to /successres/<score> route with integer score
  return redirect(url_for('successres', score=int(total_score)))


# Run the app only if this file is executed directly
if __name__ == '__main__':
  # Start Flask development server with debug mode ON
  app.run(debug=True)