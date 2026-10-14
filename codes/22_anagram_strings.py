
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True
if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    print(is_anagram(str1, str2))
