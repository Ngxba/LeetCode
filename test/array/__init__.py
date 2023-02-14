class Solution:
    def __init__(self, testCases: list) -> None:
        self.testCases = testCases
        self.testCasesLength = len(testCases)
        self.result = [testCase["result"] for testCase in testCases]
        self.inputArr = [testCase["inputArr"] for testCase in testCases]

    def solution_function(self, inputArr: list) -> None: return None

    def trigger_test_function(self) -> None:
        for i in range(self.testCasesLength):
            output = self.solution_function(self.inputArr[i])
            assert output == self.result[i], f"Input Array: {self.inputArr[i]}, " \
                                             f"result: {self.result[i]}, " \
                                             f"output: {output}"
