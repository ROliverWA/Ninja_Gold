from flask import Flask, render_template, request, redirect, session, url_for
import random
import datetime
app = Flask(__name__)  
app.secret_key="thekeytothecity"
now = str(datetime.datetime.now())
app = Flask(__name__)
app.secret_key="thekeytomyheart"
gold = 0


@app.route('/')
def root():
    session['my_trust'] = gold
    session['current_string'] = ""
    return render_template('index.html')
    
@app.route('/process_money', methods=['POST'])
def shake_your_moneymaker():    
    session['now'] = str(now)
    location = request.form['building']
    if location == 'farm':
        session['how_much'] = random.randint(10, 20)
    elif location == 'cave':
        session['how_much'] = random.randint(5, 10)
    elif location == 'house':
        session['how_much'] = random.randint(2, 5)
    elif location == 'casino':
        win_or_lose = random.randint(1,2)
        if win_or_lose == 1:
            session['how_much'] = random.randint(0, 50)
        elif win_or_lose == 2:
            session['how_much'] = random.randint(0, 50) * - 1
    session['my_trust'] += session['how_much']
    session['current_string'] += session['now']
    
       
    return render_template('index.html')


    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug = True)