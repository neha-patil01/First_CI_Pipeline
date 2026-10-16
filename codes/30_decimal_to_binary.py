def decimal_to_binary(number):
    """Convert a non-negative decimal number to binary."""
    if number < 0:
        raise ValueError("Number cannot be negative")

    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    return binary


if __name__ == "__main__":
    print(decimal_to_binary(10))