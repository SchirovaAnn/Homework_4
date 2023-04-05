import random
import shutil
import os


def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([100, 200, 300]) == 600
    assert len([sum([1, 2, 3])]) == 1


def test_random_sample():
    numbers = [1, 2, 3, 4, 5]
    assert len(random.sample(numbers, 2)) == 2
    for el in random.sample(numbers, 2):
        assert el in numbers


def test_copyfile():
    shutil.copyfile('test.txt', 'test_2.txt')
    with open('test.txt', 'r') as f:
        text_original = f.read()
    with open('test_2.txt', 'r') as f:
        text_copy = f.read()
    assert text_original == text_copy


