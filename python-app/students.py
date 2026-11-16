def average_grade(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students;")
    result = cursor.fetchone()
    return float(result[0]) if result and result[0] is not None else 0.0
