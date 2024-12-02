from flask import Blueprint, render_template, current_app, request

bp = Blueprint('list', __name__, url_prefix='/schedule')

@bp.route('/list')
def list_schedule():
    # 'schedules'를 Flask 앱 컨텍스트에서 가져오기
    schedules = current_app.config.get('SCHEDULES', [])

    # 업체 목록 추출 (중복 제거)
    companies = sorted({schedule['company'] for schedule in schedules})  # 정렬된 중복 제거 리스트

    # 서비스 목록 추출 (중복 제거)
    services = sorted(
        {service for schedule in schedules for service in schedule.get('services', [])}
    )

    return render_template(
        'schedule_list.html', 
        schedules=schedules, 
        companies=companies,
        services=services
    )
