import time
import random
import matplotlib.pyplot as plt

#  Test function to verify sorting algorithms
def test_sorting_algorithm(sort_func, n=10):
    # Perform n random test cases
    for _ in range(n):
        global length
        length = random.randint(10, 100)
        global arr
        arr = [random.randint(100, 100_000) for _ in range(length)]
        expected = sorted(arr)
        # Verify that the sorted array matches the expected result
        assert sort_func(arr) == expected

    print("All test cases passed")

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[right]) = (arr[right], arr[i + 1])
    return i + 1

def quicksort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        quicksort(arr, left, partition_index - 1)
        quicksort(arr, partition_index + 1, right)
    return arr


test_sorting_algorithm(quicksort(arr, 0, length))