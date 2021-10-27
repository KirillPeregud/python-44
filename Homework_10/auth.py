from flask import request, session, redirect, render_template
from datetime import datetime
import hashlib
from auth_password import app, db


class Authorization(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    login_user = db.Column(db.String(20), unique=True)
    password_user = db.Column(db.String)
    time_registration = db.Column(db.DateTime)

    def __init__(self, login_user, password_user, time_registration):
        self.login_user = login_user
        self.password_user = password_user
        self.time_registration = time_registration


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
        hash_password = str(hashlib.md5(password.encode()).digest())
        check_user = Authorization.query.filter_by(login_user=username).first()
        if check_user is None:
            return f'User named {username} not registered.'
        else:
            if check_user.login_user == username and check_user.password_user == hash_password:
                return redirect('/authorization')
            else:
                return 'Wrong username or password.'
    return render_template('login.html')


@app.route('/authorization', methods=['POST', 'GET'])
def authorization():
    return render_template('authorization.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        new_username = request.form['new_username']
        password_1 = request.form['password_1']
        password_2 = request.form['password_2']
        session['username'] = new_username
        if len(new_username) in range(4, 15) and len(password_1) in range(4, 15):
            new_user_check = Authorization.query.filter_by(login_user=new_username).first()
            if new_user_check is None and password_1 == password_2:
                hash_password = str(hashlib.md5(password_1.encode()).digest())
                time_reg = datetime.now()
                new_user = Authorization(new_username, hash_password, time_reg)
                db.session.add(new_user)
                db.session.commit()
                return redirect('/authorization')
            else:
                return redirect('/registration')
        else:
            return 'Form fields are filled incorrectly.'
    return render_template('registration.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
