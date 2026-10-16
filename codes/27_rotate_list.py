def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)

    return items[-k:] + items[:-k] if k != 0 else items.copy()


if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    k = 2
    print(rotate_list(items, k))