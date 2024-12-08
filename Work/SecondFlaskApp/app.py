from flask import Flask,request,render_template,jsonify,session,redirect,url_for


app = Flask(__name__)
app.secret_key = 'your_secret_key' #for session management
users = []
@app.route('/signup',methods=['GET','POST','PUT'])
def signup():
    if request.method == 'POST':
        user_data = {
            "first_name":request.form['first_name'],
            "last_name": request.form['last_name'],
            "password": request.form['password'],
            "confirm_password": request.form['confirm_password'],
            "email_id": request.form['email_id'],
            "phone_no": request.form['phone_no'],
            "manager_name": request.form['manager_name'],

        }

        #Basic Validation

        if user_data['password'] != user_data['confirm_password']:
            return "Password does not match",400

        # Check if the email alrady exists
        if any(user['email_id'] == user_data['email_id']  for user in users):
            return 'Email ID is already exists',400

        # Check if the phone alrady exists
        if any(user['phone_no'] == user_data['phone_no'] for user in users):
            return 'phone_no is already exists', 400

        #Save user data in db

        users.append(user_data)
        return redirect(url_for('login'))

    return render_template('signup.html')

#API to fetch all users(Admin or Manager API)

@app.route('/api/users',methods=['GET'])
def get_users():
    return jsonify(users)

#Route for login Page

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        email = request.form['email_id']
        password =request.form['password']

    #validate credential
        user = next((i for i in users if i['email_id']== email and i['password']==password),None)

        if user:
            session['user']=user
            return redirect(url_for('dashboard'))

        else:
            return 'Invalid Credential',400

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html',users=users)

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))
# @app.route('/update_user', method=['PUT','PATCH','PUT'])
# def update_user():
#     update_fname=request.form['update_name']
#     user = next((i for i in users if i['email_id'] == session.get('email_id') and i['password'] == session.get('password')), None)
#     if 'user' not in session:
#         return url_for('login')
#     if request.method is 'PATCH':
#             user.update({"first_name":update_fname})
#     if request.method is 'PUT':
#         user_data = {
#             "first_name": request.form['first_name'],
#             "last_name": request.form['last_name'],
#             "password": request.form['password'],
#             "confirm_password": request.form['confirm_password'],
#             "email_id": request.form['email_id'],
#             "phone_no": request.form['phone_no'],
#             "manager_name": request.form['manager_name'],
#         }
#         user.update(user_data)
#     return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True,port=5000)