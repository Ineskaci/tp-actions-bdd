def average_grade(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT AVG(grade) FROM students;")
        result = cursor.fetchone()
        return float(result[0]) if result[0] is not None else 0.0
