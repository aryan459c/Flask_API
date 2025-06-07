from flask import Flask, render_template, redirect, url_for, flash, request, session
from forms import SignupForm, LoginForm
import json
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Load user data from the JSON file
def load_users():
    if os.path.exists(app.config['DATA_FILE']):
        with open(app.config['DATA_FILE'], 'r') as file:
            return json.load(file)
    return {}

# Save user data to the JSON file
def save_users(users):
    with open(app.config['DATA_FILE'], 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        users = load_users()
        if form.username.data in users:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            hashed_password = generate_password_hash(form.password.data)
            users[form.username.data] = {
                'username': form.username.data,
                'email': form.email.data,
                'password': hashed_password
            }
            save_users(users)
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = load_users()
        user = users.get(form.username.data)
        if user and check_password_hash(user['password'], form.password.data):
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))
    username = session['username']
    return render_template('dashboard.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
