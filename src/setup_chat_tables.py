from db_connect import connect_to_db

def setup_tables():
    with open("src/sql/init_chat_tables.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    conn = connect_to_db()
    cursor = conn.cursor()
    for stmt in sql.strip().split(';'):
        if stmt.strip():
            cursor.execute(stmt)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ جدول‌های چت‌بات ساخته شد.")

if __name__ == "__main__":
    setup_tables()
