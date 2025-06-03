from db_connect import connect_to_db
from datetime import date


def report_attendance(target_date=None):
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)

    if not target_date:
        target_date = date.today()

    print(f"\n📌 گزارش حضور برای تاریخ {target_date}:\n")
    cursor.execute("""
        SELECT e.full_name, a.status 
        FROM attendance a
        JOIN employees e ON a.employee_id = e.id
        WHERE a.date = %s
    """, (target_date,))

    results = cursor.fetchall()
    for row in results:
        print(f"{row['full_name']} - {row['status']}")

    cursor.close()
    conn.close()


def report_sales(target_date=None):
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)

    if not target_date:
        target_date = date.today()

    print(f"\n📈 گزارش فروش برای تاریخ {target_date}:\n")
    cursor.execute("""
        SELECT e.full_name, s.amount 
        FROM sales_reports s
        JOIN employees e ON s.employee_id = e.id
        WHERE s.date = %s
    """, (target_date,))

    results = cursor.fetchall()
    total = 0
    for row in results:
        print(f"{row['full_name']} - فروش: {row['amount']}")
        total += float(row['amount'])

    print(f"\n🔢 مجموع فروش روزانه: {total} تومان")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    today = date.today()
    report_attendance(today)
    report_sales(today)
