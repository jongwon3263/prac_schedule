from flask import Blueprint, render_template

bp = Blueprint('company', __name__, url_prefix='/manage')

@bp.route('/company')
def company_list():
    return render_template('company.html')