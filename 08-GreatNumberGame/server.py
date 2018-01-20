from flask import Flask, render_template, request, redirect, session

import random

app = Flask(__name__)
app.secret_key = 'SecretKeyIsSecret123'

@app.route('/')
def index():
    if "randomNum" not in session:
        session['randomNum'] = random.randrange(0,101)
        session['guessNum'] = 0
        session['statusAnswer'] = 0
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def index_submit():
    if "randomNum" not in session:
        session['randomNum'] = random.randrange(0,101)
        session['guessNum'] = 0
        session['statusAnswer'] = 0
    print "submit"
    print request.form['guessNum']
    if (request.form['guessNum']) == '':
        return redirect('/')
    if (request.form['guessNum']) == str(session['randomNum']):
        session['statusAnswer'] = 3 # 'Correct Number'
    elif (request.form['guessNum']) > str(session['randomNum']):
        session['statusAnswer'] = 1 # 'Too high!'
    elif (request.form['guessNum']) < str(session['randomNum']):
        session['statusAnswer'] = 2 # 'Too low!'
    return redirect('/')

@app.route('/playAgain',methods=['POST'])
def index_playAgain():
    if "randomNum" not in session:
        session['randomNum'] = random.randrange(0,101)
        session['guessNum'] = 0
        session['statusAnswer'] = 0
    print "play again"
    session['randomNum'] = random.randrange(0,101)
    session['guessNum'] = 0
    session['statusAnswer'] = 0
    return redirect('/')

app.run(debug=True)
