from typing import List


class Solution:
    def __init__(self, logs):
        self.solution = self.maximumPopulations(logs)

    def maximumPopulations(self, logs: List[List[int]]) -> int:
        if len(logs) < 0: return 0
        chronolog = sorted(logs, key=lambda log: log[0])
        
        deaths = [chronolog[0][1]] # idea -- pop deaths off as they become relevant, otherwise keep a queue
        current_pop = 0
        max_pop = 0
        
        for log in chronolog:
            pass

        return 0

data = [[1950, 1961], [1960, 1971], [1970, 1981]]
test = Solution(logs=data)
print(test.solution)