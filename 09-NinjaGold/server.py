from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'SecretKeyIsSecret123'

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    if "activities" not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():
    if "gold" not in session:
        session['gold'] = 0
    if "activities" not in session:
        session['activities'] = []
    print "process_money"
    now = datetime.now()
    if request.form['building'] == 'farm':
        randNum = random.randrange(10,21)
        session['gold'] += randNum
        session['activities'].append('Earned '+str(randNum)+' from the farm! ('+str(now)+')')
        print randNum, session['gold']
    elif request.form['building'] == 'cave':
        randNum = random.randrange(5,11)
        session['gold'] += randNum
        session['activities'].append('Earned '+str(randNum)+' from the cave! ('+str(now)+')')
        print randNum, session['gold']
    elif request.form['building'] == 'house':
        randNum= random.randrange(2,6)
        session['gold'] += randNum
        session['activities'].append('Earned '+str(randNum)+' from the house! ('+str(now)+')')
        print randNum, session['gold']
    elif request.form['building'] == 'casino':
        randNum = random.randrange(-50,51)
        session['gold'] += randNum
        if randNum >= 0:
            session['activities'].append('Earned '+str(randNum)+' from the casino! ('+str(now)+')')
        else:
            session['activities'].append('Entered a casino and lost '+str(randNum)+' golds... Ouch... ('+str(now)+')')
        print randNum, session['gold']
    return redirect('/')

@app.route('/reset',methods=['POST'])
def reset():
    if "gold" not in session:
        session['gold'] = 0
    if "activities" not in session:
        session['activities'] = []
    print "reset"
    session['gold'] = 0
    session['activities'] = []
    return redirect('/')
app.run(debug=True)
