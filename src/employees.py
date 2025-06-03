from db_connect import connect_to_db

def add_employee(full_name, position, hire_date):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO employees (full_name, position, hire_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (full_name, position, hire_date))
    conn.commit()
    print(f"کارمند {full_name} اضافه شد.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_employee("الناز رضایی", "مدیر فروش", "2024-12-01")
