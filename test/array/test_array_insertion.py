from main.array import duplicate_zero
from test.array import Solution


def test_duplicate_zero():
    testCase = [
        # {
        #     "inputArr": [1,0,2,3,0,4,5,0],
        #     "result": [1,0,0,2,3,0,0,4],
        # },
        # {
        #     "inputArr": [1,2,3],
        #     "result": [1,2,3],
        # },
        {
            "inputArr": [0,4,1,0,0,8,0,0,3],
            "result": [0,0,4,1,0,0,0,0,8],
        }
    ]
    sol = Solution(testCase)
    sol.solution_function = duplicate_zero.solution
    sol.trigger_test_function()

test_duplicate_zero()