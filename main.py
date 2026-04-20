from sorting import bubble_sort, selection_sort
from student_grades import StudentsGrades

import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


numbers = [5, 4, 9, 1, 6]
print(f"Původní seznam: ", numbers)
print(f"Seřazený seznam: ", selection_sort(numbers))
print(f"Bubble sort: ", bubble_sort(numbers))






results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)
print(results.get_grade(2))  # A (91 bodů)
print(results.get_grade(6))  # A (100 bodů)
print(results.get_grade(7))  # F (38 bodů)

print(results.find(100))  # [6]
print(results.find(50))   # [4]
print(results.find(77))   # []

