from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def index2():
    print "*----------------"
    print request.form['xred']
    print request.form['xgreen']
    print request.form['xblue']
    return render_template('index.html',xred=request.form['xred'],xgreen=request.form['xgreen'],xblue=request.form['xblue'])

app.run(debug=True)
