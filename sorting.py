
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers[:]
    for pozice_ukladani in range(len(numbers)):


