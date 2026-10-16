
import importlib

module = importlib.import_module("26_sum_list")
sum_of_list = module.sum_of_list


def test_normal_list():
    assert sum_of_list([1, 2, 3, 4, 5]) == 15


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_element():
    assert sum_of_list([7]) == 7


def test_negative_numbers():
    assert sum_of_list([-2, -3, 5]) == 0


def test_zero_values():
    assert sum_of_list([0, 0, 0]) == 0
