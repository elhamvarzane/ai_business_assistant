import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # اگر نام کاربری دیگه‌ای داری، اینجا تغییر بده
        password="Egv123456",           # اگر رمز داری، اینجا وارد کن
        database="ai_business"  #  موقت
    )
