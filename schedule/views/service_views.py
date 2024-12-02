from flask import Blueprint, render_template

bp = Blueprint('service', __name__, url_prefix='/service')

@bp.route('/')
def service_list():
    print("service view")
    return render_template('service.html')