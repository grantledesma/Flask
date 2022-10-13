from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
        return "<b>Login</b>"

@auth.route('/logout')
def logout():
        return "<b>logout</b>"

@auth.route('/sign-up')
def sign_up():
        return "<b>sign up</b>"