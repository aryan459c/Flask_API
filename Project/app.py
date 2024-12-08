
from flask import Flask, request, session, redirect, url_for, render_template

app=Flask(__name__)
app.secret_key="ok"
users=[{'uname':'sunil','pword':'1234' }]
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
         return redirect(url_for('login'))
    return render_template('dashboard.html', users=users)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        uname=request.form['uname']
        pword=request.form['pword']
        global user
        user = next((i for i in users if i['uname'] == uname and i['pword'] == pword), None)
        if user:
            session['user']=user
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Username or Password"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)