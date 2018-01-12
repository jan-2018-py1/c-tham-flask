from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/',methods=['POST'])
def process():
  print "** Got Post Info **"
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  print name
  print location
  print language
  print comment
  return render_template('result.html', name=request.form['name'], location=request.form['location'],   language=request.form['language'], comment=request.form['comment'])
  # return redirect('/')

@app.route('/result',methods=['GET'])
def result():
  return redirect('/')

app.run(debug=True)
