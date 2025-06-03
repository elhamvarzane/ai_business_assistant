from db_connect import connect_to_db

def add_sale(employee_id, date, amount):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO sales_reports (employee_id, date, amount) VALUES (%s, %s, %s)"
    cursor.execute(query, (employee_id, date, amount))
    conn.commit()
    print(f"فروش {amount} برای کارمند {employee_id} ثبت شد.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_sale(1, "2025-06-03", 120000.00)
