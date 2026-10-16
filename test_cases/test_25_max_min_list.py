import importlib

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([4, 2, 9, 1, 7]) == (9, 1)


def test_single_element():
    assert find_max_min([5]) == (5, 5)


def test_negative_numbers():
    assert find_max_min([-4, -2, -9]) == (-2, -9)


def test_duplicate_numbers():
    assert find_max_min([3, 3, 3]) == (3, 3)


def test_empty_list():
    try:
        find_max_min([])
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError for an empty list"
