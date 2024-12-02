from flask import Blueprint, render_template

bp = Blueprint('register', __name__, url_prefix='/schedule')

@bp.route('/register')
def register_schedule():
    return render_template('schedule_regi.html')