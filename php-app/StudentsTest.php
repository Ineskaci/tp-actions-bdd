def average_grade(conn):
    with conn.cursor() as cursor:
        # On envoie la requête SQL pour calculer la moyenne (comme le font add_student et get_student)
        cursor.execute("SELECT AVG(grade) FROM students;")
        result = cursor.fetchone()
        # On retourne le résultat sous forme de nombre décimal (float)
        return float(result[0]) if result[0] is not None else 0.0
