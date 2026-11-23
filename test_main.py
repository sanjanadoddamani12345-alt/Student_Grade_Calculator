
from main import calculate_average, assign_grade, get_remark


def test_calculate_average():
    assert calculate_average([90, 80, 70]) == 80


def test_grade_s():
    assert assign_grade(95) == "S"


def test_grade_a():
    assert assign_grade(85) == "A"


def test_grade_b():
    assert assign_grade(70) == "B"


def test_grade_c():
    assert assign_grade(55) == "C"


def test_grade_d():
    assert assign_grade(45) == "D"


def test_grade_f():
    assert assign_grade(30) == "F"


def test_performance_remark():
    assert get_remark(95) == "Outstanding Performance"


def test_low_performance_remark():
    assert get_remark(35) == "Needs Improvement"
