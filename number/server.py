from flask import Flask, session, redirect, render_template, request
import random

app = Flask(__name__)
app.secret_key = "dankmemesareneverdankenough"

@app.route("/")
def hola():
    session['number'] = random.randrange(0, 101)
    print("random: ", session['number'])
    return render_template('index.html',**session)

@app.route("/keepingtrack", methods=["post"])
def checking():
    guess = int(request.form["guess"])
    if session['number'] == guess:
        session['filler']= "YOU GOT LUCKY"
        session['ans'] = 'right'
    elif session['number'] > guess:
        session['filler']="TOO LOW JUST LIKE YOUR SAT SCORE"
    elif session['number'] < guess:
        session['filler']="TOO HIGH JUST LIKE YOUR SALT LEVEL"
    
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)