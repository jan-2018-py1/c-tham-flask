from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_WOJS.html')

@app.route('/red',methods=['POST'])
def index_red():
    print "red"
    return render_template('index_WOJS.html',colour='red')

@app.route('/blue',methods=['POST'])
def index_blue():
    print "blue"
    return render_template('index_WOJS.html',colour='blue')

@app.route('/orange',methods=['POST'])
def index_orange():
    print "orange"
    return render_template('index_WOJS.html',colour='orange')

@app.route('/purple',methods=['POST'])
def index_purple():
    print "purple"
    return render_template('index_WOJS.html',colour='purple')

@app.route('/custom',methods=['POST'])
def index_custom():
    print "custom"+request.form['customColor']
    return render_template('index_WOJS.html',colour=request.form['customColor'])

app.run(debug=True)