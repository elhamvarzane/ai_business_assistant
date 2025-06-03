import mysql.connector

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Egv123456",  # رمز عبور MySQL خودت رو بذار اینجا
            database="ai_business"
        )
        print("✅ اتصال موفق به دیتابیس.")
        return conn
    except mysql.connector.Error as err:
        print("❌ خطا در اتصال به دیتابیس:", err)

if __name__ == "__main__":
    connect_to_db()
