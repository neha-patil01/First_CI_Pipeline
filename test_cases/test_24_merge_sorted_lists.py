
import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_one_empty_list():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_negative_numbers():
    assert merge_sorted_lists([-3, -1], [-2, 0]) == [-3, -2, -1, 0]


def test_original_lists_unchanged():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merge_sorted_lists(list1, list2)
    assert list1 == [1, 3, 5]
    assert list2 == [2, 4, 6]
