from flask import Blueprint, render_template
from flask_login import login_required, current_user


view = Blueprint('view', import_name='view', url_prefix='/')


@view.route('/')
def index():
    return render_template('index.html', user=current_user)
