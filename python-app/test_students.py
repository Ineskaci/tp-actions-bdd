import pytest
from students import add_student, get_student, average_grade

def test_add_and_get_student(conn):
    """Test 1: Ajouter un étudiant, puis le relire."""
    add_student(conn, "Amel", 14)
    student = get_student(conn, "Amel")
    assert student is not None
    assert student[0] == "Amel"
    assert float(student[1]) == 14.0

def test_get_nonexistent_student(conn):
    """Test 2: Lire un étudiant qui n'existe pas (doit retourner None)."""
    student = get_student(conn, "Inconnu")
    assert student is None

def test_moyenne(conn):
    """Test 3: Ajouter deux étudiants et vérifier la moyenne (10 et 14 -> 12)."""
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)
    # (10 + 14) / 2 = 12.0[cite: 2]
    assert average_grade(conn) == 12.0
