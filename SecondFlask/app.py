from flask import Flask, render_template, request


app = Flask(__name__)
users=[]
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        user_data={
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "password": request.form['password'],
            "confirm_password": request.form['confirm_password'],
            "email_id": request.form['email_id'],
            "phone_no": request.form['phone_no'],
            "manager_name": request.form['manager_name'],

        }
    #Basic validation
        if user_data['password']!=user_data['confirm_password']:
            return "Password dosen't match",400
    #Check if the email id is alraedy exits
        if any(user['email_id'] != user_data['email_id'] for user in users):
            return "Email id is already exists",400
    #Check if the phone no is already exist
        if any(user['phone_no'] != user_data['phone_no'] for user in users):
            return "Phone number is already exists",400
        users.append(user_data)
    return render_template('signup.html')
if __name__=='__main__':
    app.run(debug=True,port=5000)
