from sorting import bubble_sort, selection_sort
from student_grades import StudentsGrades

import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


numbers = [5, 4, 9, 1, 6]






results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])



def main():
    vysled = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentů: ", results.count())
    for a in range(vysled.count()):
        body = vysled.get_by_index(a)
        znamka = vysled.get_grade(a)
        print(f"Student {a}: {body} points - {znamka}")
    print("Studenti se 100 body: ", vysled.find(100))
    print("Seřazené výsledky: ", vysled.get_sorted())

if __name__ == "__main__":
    main()



