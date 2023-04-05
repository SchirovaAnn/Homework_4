import math

# filter
def filter_function(number):
    if number % 2 == 0:
        return True
    else:
        return False


my_numbers = [1, -2, 3, 56, -8, 9]
even_numbers = filter(filter_function, my_numbers)
print(list(even_numbers))


def test_filter():
    assert len(list(filter(filter_function, my_numbers))) > 0

    for num in list(filter(filter_function, my_numbers)):
        assert num in my_numbers


# map
def test_map():
    assert len(list(map(abs, my_numbers))) == len(my_numbers)

    for num in list(map(abs, my_numbers)):
        assert num in [abs(x) for x in my_numbers]


# sorted
def test_sorted():
    assert len(sorted(my_numbers)) == len(my_numbers)

    for num in sorted(my_numbers):
        assert num in my_numbers


# pi
def test_pi():
    assert math.pi == 3.141592653589793


# sqrt
def test_sqrt():
    assert math.sqrt(9) == 3
    assert math.sqrt(4) == 2
    assert math.sqrt(144) == 12


# pow
def test_pow():
    assert math.pow(2, 1) == 2
    assert math.pow(2, 2) == 4
    assert math.pow(4, 2) == 16


# hypot
def test_hypot():
    assert math.hypot(10, 5) == 11.180339887498949
    assert math.hypot(15, 10) == 18.027756377319946
    assert math.hypot(1, 1) == 1.4142135623730951

