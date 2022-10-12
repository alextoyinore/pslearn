from hashlib import sha256
from . import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', import_name='auth', url_prefix='/')


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('view.index'))

    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('An account with this email already exists.', category='error')
        elif len(firstname) < 2:
            flash('First name cannot be less than two (2) characters',
                  category='error')
        elif len(lastname) < 2:
            flash('Last name cannot be less than two (2) characters',
                  category='error')
        elif len(email) < 2:
            flash('Email is too short', category='error')
        elif len(password) < 8:
            flash('Password cannot be less than 8 characters', category='error')
        else:
            new_user = User(email=email, first_name=firstname, last_name=lastname,
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #login_user(user, remember=True)
            flash('Your account has been successfully created.', category='success')
            return redirect(url_for('auth.login'))
    return render_template('signup.html', user=current_user)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('view.index'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.index'))
            else:
                flash('Password is incorrect', category='error')
        else:
            flash(
                'There is no account matching this email on this platform.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/forgot-password', methods=['POST', 'GET'])
def forgot_password():
    return render_template('forgot_password.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
