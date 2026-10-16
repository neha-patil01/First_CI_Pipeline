def bubble_sort(numbers):
    arr = numbers.copy()

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    numbers = [5, 2, 9, 1]
    print(bubble_sort(numbers))