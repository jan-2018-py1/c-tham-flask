from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretKeyIsSecret123'

@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/add2',methods=['POST'])
def index_add2():
    print "add 2 button"
    session['counter'] += 1
    # session counter to increase by 1 at index()
    return redirect('/')

@app.route('/reset',methods=['POST'])
def index_reset():
    print "reset button"
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
