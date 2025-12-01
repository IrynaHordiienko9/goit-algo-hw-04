import random
import timeit


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def timsort(arr):
    return sorted(arr)


sizes = [1000, 5000, 10000]
for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]
    print(f"Size: {size}")
    print("Merge Sort:", timeit.timeit(lambda: merge_sort(arr.copy()), number=1))
    print("Insertion Sort:", timeit.timeit(lambda: insertion_sort(arr.copy()), number=1))
    print("Timsort:", timeit.timeit(lambda: timsort(arr.copy()), number=1))
