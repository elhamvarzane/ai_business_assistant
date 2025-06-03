from db_connect import connect_to_db

def list_tables(database_name):
    conn = connect_to_db()
    conn.database = database_name
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")

    print(f"\n📂 جدول‌های داخل دیتابیس {database_name}:")
    for (table,) in cursor.fetchall():
        print(f" - {table}")

    cursor.close()
    conn.close()
def describe_table(database_name, table_name):
    conn = connect_to_db()
    conn.database = database_name
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE {table_name}")

    print(f"\n🔍 ساختار جدول {table_name}:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    db ="ai_business"
    list_tables (db)  # دستی بذار فعلاً
    describe_table(db, "attendance")  # تستی
