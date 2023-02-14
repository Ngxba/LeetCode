from main.array import max_consectutive_ones, sorted_squares
from main.array import find_numbers_with_even_number_of_digits
from test.array import Solution


def test_max_consecutive_ones():
    testCase = [
        {
            "inputArr": [1, 0, 1, 1, 0, 1],
            "result": 2,
        },
        {
            "inputArr": [1, 1, 0, 1, 1, 1],
            "result": 3,
        }
    ]
    sol = Solution(testCase)
    sol.solution_function = max_consectutive_ones.solution
    sol.trigger_test_function()


def test_find_even_numbers():
    testCase = [
        {
            "inputArr": [12, 345, 2, 6, 7896],
            "result": 2,
        },
        {
            "inputArr": [555, 901, 482, 1771],
            "result": 1,
        },
        {
            "inputArr": [100000],
            "result": 1,
        },
    ]

    sol = Solution(testCase)
    sol.solution_function = find_numbers_with_even_number_of_digits.solution
    sol.trigger_test_function()


def test_sorted_squares():
    testCase = [
        {
            "inputArr": [-4, -1, 0, 3, 10],
            "result": [0, 1, 9, 16, 100],
        },
        {
            "inputArr": [-7, -3, 2, 3, 11],
            "result": [4, 9, 9, 49, 121],
        },
    ]
    sol = Solution(testCase)
    sol.solution_function = sorted_squares.solution
    sol.trigger_test_function()
