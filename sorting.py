
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(nums):
    nums = nums[:]
    for poz_ukladani in range(len(nums)):
        min_index = poz_ukladani
        for poz_prochazena in range(poz_ukladani + 1, len(nums)):
            if nums[poz_prochazena] < nums[min_index]:
                min_index = poz_prochazena

        nums[poz_ukladani], nums[min_index] = nums[min_index], nums[poz_ukladani]
    return nums

def bubble_sort(nums):
    nums = nums[:]
    for a in range(len(nums)):
        for b in range(0, len(nums) - a - 1):
            if nums[b] > nums[b + 1]:
                nums[b], nums[b + 1] = nums[b + 1], nums[b]
    return nums