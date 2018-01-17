from flask import Flask, render_template, request, redirect, session

import random

app = Flask(__name__)
app.secret_key = 'SecretKeyIsSecret123'

@app.route('/')
def index():
    if "randomNum" not in session:
        session['randomNum'] = random.randrange(0,101)
        session['guessNum'] = 0
    return render_template('index.html', randomNum=session['randomNum'])

@app.route('/submit',methods=['POST'])
def index_submit():
    print "submit"
    print request.form['guessNum']
    if (request.form['guessNum']) == str(session['randomNum']):
        session['statusAnswer'] = str(session['randomNum'])+' was the number!'
    elif (request.form['guessNum']) > str(session['randomNum']):
        session['statusAnswer'] = 'Too high!'
    elif (request.form['guessNum']) < str(session['randomNum']):
        session['statusAnswer'] = 'Too low!'
    return render_template('index.html', statusAnswer=session['statusAnswer'])

@app.route('/playAgain',methods=['POST'])
def index_playAgain():
    print "play again"
    session['randomNum'] = random.randrange(0,101)
    session['guessNum'] = 0
    return render_template('index.html', randomNum=session['randomNum'])

app.run(debug=True)
