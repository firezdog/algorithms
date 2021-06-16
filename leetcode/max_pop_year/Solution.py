from typing import List


class Solution:
    def __init__(self, logs):
        self.solution = self.maximumPopulation(logs)

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        if len(logs) < 0: return 0
        chronolog = sorted(logs, key=lambda log: log[0])
        
        deaths = [] # idea -- pop deaths off as they become relevant, otherwise keep a queue
        next_death = chronolog[0][1]
        current_pop = 0
        max_pop = 0
        
        for log in chronolog:
            current_pop += 1
            deaths.append(log[1])

            now = log[0]
            if next_death <= now: 
                current_pop -= 1
                next_death = deaths.pop(0)

            if max_pop < current_pop: max_pop = current_pop

        return max_pop  # TODO: needs to return the year

data = [[1950, 1961], [1961, 1971]]
test = Solution(logs=data)
print(test.solution)