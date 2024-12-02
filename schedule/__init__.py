from flask import Flask
from dotenv import load_dotenv
import os, random
from .views import main_views, register_views, list_views, company_views, service_views, detail_views
from faker import Faker
from datetime import date

# .env 파일 로드하여 환경변수 설정
load_dotenv()

def create_app():
    # Flask 애플리케이션 생성
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

    # 블루프린트 등록
    app.register_blueprint(main_views.bp)
    app.register_blueprint(register_views.bp)
    app.register_blueprint(list_views.bp)
    app.register_blueprint(company_views.bp)
    app.register_blueprint(service_views.bp)
    app.register_blueprint(detail_views.bp)

    # 필터 정의 및 등록
    def number_format(value, separator=','):
        """숫자를 세 자리마다 구분자로 포맷하는 필터"""
        try:
            if isinstance(value, (int, float)):
                return f"{value:,.0f}".replace(",", separator)
            return value
        except Exception as e:
            return value  # 예외 발생 시 원래 값 반환

    app.jinja_env.filters['number_format'] = number_format

    # Faker 객체 생성 (애플리케이션 시작 시 한 번만 생성)
    fake = Faker("ko_KR")

    def generate_random_schedule():
        schedule_id = random.randint(1, 300)  # 고유한 UUID 생성
        areas = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "안산", "수원", "성남"]
        services = ["청소", "줄눈", "탄성코트", "생활코팅", "새집증후군 솔루션", "가전 분해청소"]
        details = ["신축 입주청소", "이사 청소", "생활 청소", "폴리우레아", "케라폭시", "바이오세라믹", "나노코팅"]
        statuses = ["완료", "진행 중", "대기", "미배정"]
        companies = ["로이클린", "바르지오", "라인케이", "클린뷰", "손크린", "팍리숨"]

        area = random.choice(areas)
        address = f"{area}시 {fake.street_name()} {random.randint(1, 100)}번길 {random.randint(1, 30)}층 {random.randint(1, 20)}호"
        status = random.choice(statuses)
        service = random.sample(services, random.randint(1, 5))  # 1~5개의 서비스 선택
        detail = random.choice(details)

        # 날짜 생성 (10월 1일부터 12월 31일까지)
        start_date_obj = fake.date_between(start_date=date(2024, 10, 1), end_date=date(2024, 12, 31))
        finish_date_obj = fake.date_between(start_date=start_date_obj, end_date=date(2024, 12, 31))

        # 날짜를 문자열로 변환
        start_date = start_date_obj.strftime("%Y-%m-%d")
        finish_date = finish_date_obj.strftime("%Y-%m-%d")

        customer_phone = fake.phone_number()
        company = random.choice(companies)
        company_pay = random.randint(200000, 800000)
        total_sales = company_pay + random.randint(50000, 200000)
        down_payment = random.randint(50000, 100000)
        balance = total_sales - down_payment

        return {
            "id": schedule_id,  # 고유한 ID 추가
            "area": area,
            "address": address,
            "status": status,
            "services": service,
            "detail": detail,
            "startDate": start_date,
            "finishDate": finish_date,
            "customerPhone": customer_phone,
            "company": company,
            "companyPay": company_pay,
            "totalSales": total_sales,
            "downPayment": down_payment,
            "balance": balance,
        }

    # 데이터 300개 생성 (앱 시작 시 한 번만 생성)
    schedules = [generate_random_schedule() for _ in range(300)]

    # schedules 데이터를 앱 config에 저장
    app.config['SCHEDULES'] = schedules

    return app
