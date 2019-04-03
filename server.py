from flask import Flask, render_template,session,request,url_for
import random
app = Flask(__name__)
app.secret_key="thekeytomyheart"
gold = 0

@app.route('/')
def root():
    session['my_trust'] = gold
    return render_template('index.html')
    
@app.route('/process_money', methods=['POST'])
def shake_your_moneymaker():
    return render_template('index.html')
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug = True)