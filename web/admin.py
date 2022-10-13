from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

admin = Blueprint('admin', import_name='admin', url_prefix='/')


@admin.route('/admin')
def dash():
    return 'Admin'


@admin.route('/admin-login', methods=['POST', 'GET'])
def dash_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return render_template('admin/login.html')
