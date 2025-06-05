from db_connect import connect_to_db


def get_all_database_schemas():
    conn = connect_to_db()
    cursor = conn.cursor()

    # تمام دیتابیس‌ها رو بگیر
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall() if
                 db[0] not in ['information_schema', 'mysql', 'performance_schema', 'sys']]

    db_schemas = {}

    for db in databases:
        try:
            print(f"\n🔍 بررسی دیتابیس: {db}")
            conn.database = db
            cursor.execute("SHOW TABLES")
            tables = [t[0] for t in cursor.fetchall()]
            db_schemas[db] = {}

            for table in tables:
                cursor.execute(f"DESCRIBE {table}")
                structure = cursor.fetchall()
                db_schemas[db][table] = structure
                print(f" - جدول: {table} ✅")
        except Exception as e:
            print(f"⛔️ خطا در دیتابیس {db}: {e}")

    cursor.close()
    conn.close()
    return db_schemas


if __name__ == "__main__":
    schemas = get_all_database_schemas()

    # نمایش ساختار برای تست
    for db, tables in schemas.items():
        print(f"\n📁 دیتابیس: {db}")
        for table, structure in tables.items():
            print(f"  📄 جدول: {table}")
            for column in structure:
                print(f"    - {column}")
