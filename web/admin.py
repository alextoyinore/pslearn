from flask import Blueprint

admin = Blueprint('admin', import_name='admin', url_prefix='/')


@admin.route('/admin')
def dash():
    return 'Admin'
