from flask import Blueprint, render_template, current_app, abort

bp = Blueprint('detail', __name__, url_prefix='/schedule')

@bp.route('/detail/<int:schedule_id>/')
def detail_schedule(schedule_id):
    # schedules에서 schedule_id가 int로 일치하는 일정을 찾음
    schedules = current_app.config.get('SCHEDULES')
    
    # 해당 schedule_id가 있는지 확인
    schedule = next((s for s in schedules if s['id'] == schedule_id), None)
    
    # 해당 일정이 없으면 404 에러 발생
    if schedule is None:
        abort(404)
    
    return render_template('schedule_detail.html', schedule=schedule)
