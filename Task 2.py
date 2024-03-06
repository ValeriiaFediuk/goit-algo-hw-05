def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        iterations += 1

    if high >= 0:
        return iterations, arr[high] if arr[high] >= target else arr[high + 1] if high + 1 < len(arr) else None
    else:
        return iterations, None

arr = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
target = 6
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Елемент відсутній у масиві")
