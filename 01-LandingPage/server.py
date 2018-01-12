from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
  return render_template('dojos.html')
  print "Got Post Info"
  name = request.form['name']
  email = request.form['email']
  return render_template('success.html')

app.run(debug=True)
