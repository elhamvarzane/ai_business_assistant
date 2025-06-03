from db_connect import connect_to_db

def add_attendance(employee_id, date, status):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO attendance (employee_id, date, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (employee_id, date, status))
    conn.commit()
    print(f"ثبت حضور برای کارمند {employee_id} در تاریخ {date}.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_attendance(2, "2025-06-04", "present")
