from flask import Flask, render_template, request, redirect, session, url_for
import random
import datetime
app = Flask(__name__)  
app.secret_key="thekeytothecity"




@app.route('/')
def root():
    now = str(datetime.datetime.now().strftime("%a %b %Y %T"))    
    session['now'] =  now
    
    if "count" in session:
        session['count'] += 1
    else:
        session['count'] = 1
        session['current_string'] = ""
        session['my_trust'] = 0
        
        
    
    
    return render_template('index.html')
    
@app.route('/process_money', methods=['POST'])
def shake_your_moneymaker():    
       
    location = request.form['building']
    session['location'] = location
    if location == 'farm':
        session['how_much'] = random.randint(10, 20)
    elif location == 'cave':
        session['how_much'] = random.randint(5, 10)
    elif location == 'house':
        session['how_much'] = random.randint(2, 5)
    elif location == 'casino':
        win_or_lose = random.randint(1,2)
        loser = False
        if win_or_lose == 1:            
            session['how_much'] = random.randint(0, 50)
            session['my_trust'] += session['how_much']
            session['current_string'] += "<p id='win' style='color:green'> Earned " + " " + str(session['how_much']) + " from the " + location + "! " + str(session['now']) + "</p>|"
        elif win_or_lose == 2:
            loser = True
            session['how_much'] = random.randint(0, 50) * - 1
            session['current_string'] += "<p id='lose' style='color:red'> Earned "+ " "  + str(session['how_much']) + " from the " + location + "! " + str(session['now']) + "</p>|"
        return redirect('/')
     
    session['my_trust'] += session['how_much']
    session['current_string'] += "<p id='win'style='color:green'> Earned "  + " " + str(session['how_much']) + " from the " + location + "! " + str(session['now']) + "</p>|"
    print(session['current_string'])
    return redirect('/')
    
@app.route('/reset_me', methods=['POST'])
def every_new_begining():
    session.clear()
    return redirect('/')
    
    

       



    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug = True)