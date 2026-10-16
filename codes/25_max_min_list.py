def find_max_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    return maximum, minimum


if __name__ == "__main__":
    numbers = [4, 2, 9, 1, 7]
    print(find_max_min(numbers))
