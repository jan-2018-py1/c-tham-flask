from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/ninja')
def ninja1():
    return render_template('ninja1.html')

@app.route('/ninja/<color>')
def ninja2(color):
    print color
    return render_template('ninja2.html', colour=color)

app.run(debug=True)