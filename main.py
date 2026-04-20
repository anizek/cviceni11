from sorting import bubble_sort, selection_sort

import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


numbers = [5, 4, 9, 1, 6]
print(f"Původní seznam: ", numbers)
print(f"Seřazený seznam: ", selection_sort(numbers))
print(f"Bubble sort: ", bubble_sort(numbers))