from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


view = Blueprint('view', import_name='view', url_prefix='/')


UNDER_CONSTRUCTION = True


@view.route('/')
def index():
    if UNDER_CONSTRUCTION:
        return redirect(url_for('view.under_construction'))
    return render_template('index.html', user=current_user)


@view.route('/under-construction')
def under_construction():
    return render_template('under_construction.html')
