from flask import Flask, render_template, request, redirect, session # added request
import random


app=Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
def gm(p1,p2):
    sen={
        'rock':{'rock':'tie','paper':'lose','scissors':'win'},
        'paper':{'rock':'win','paper':'tie','scissors':'lose'},
        'scissors':{'rock':'lose','paper':'win','scissors':'tie'}
    }
    return sen[p1][p2]

count_win=0
count_lose=0
count_tie=0

    	
    	
@app.route('/')
def index():
    return render_template("game.html")

@app.route('/game', methods=['POST'])
def create_user():
     print(request.form)
     x = request.form['game']
     print("you picked:" +x)
     arr=["rock","paper","scissors"]
     z=random.randint(0,2)
     print("--"*30)
     print(z)
     session['first'] = x
     y=random.choice(arr)
     session['second'] = y
     session['third'] = gm(x,y)
     global count_win
     global count_lose
     global count_tie
     if session['third']=='win':
     	count_win+=1
     if session['third']=='lose':
     	count_lose+=1	
     if session['third']=='tie':
     	count_tie+=1
     session['fourth']=count_win
     session['fifth']=count_lose
     session['sixth']=count_tie
     return redirect("/show")	# changed this line!
     

@app.route("/show")
def show_user():
    #return render_template("game2.html", first=x, second=y,third=gm(x,y))
    return render_template("game2.html", first=session['first'],second=session['second'],third=session['third'],fourth=session['fourth'],fifth=session['fifth'],sixth=session['sixth'])
    
    
     #return " You picked:" +x+"          /the computer picked:" + y +"you"+gm(x,y)
     #return render_template("game.html", first=session['first'])

if __name__=="__main__":
	app.run(debug=True)