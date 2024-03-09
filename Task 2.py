def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    mid = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return iterations, arr[mid]

    if low < len(arr):
        return iterations, arr[low]
    else:
        return iterations, arr[high]


arr = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
target = 1
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Елемент відсутній у масиві")
