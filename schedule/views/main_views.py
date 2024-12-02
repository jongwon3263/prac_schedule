from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    # index 페이지에서 base.html을 렌더링
    return render_template('base.html')
