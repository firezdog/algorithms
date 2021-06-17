from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        if len(logs) < 0: return 0

        logs_by_birth = sorted(logs, key=lambda log: log[0])
        logs_by_death = sorted(logs, key=lambda log: log[1])
        
        next_death = logs_by_death[0][1]
        next_death_ptr = 1

        current_pop = 0
        max_pop = 0
        max_pop_year = 0
        
        for log in logs_by_birth:
            current_pop += 1

            now = log[0]
            while next_death <= now: 
                current_pop -= 1
                next_death_ptr += 1
                try:
                    next_death = logs_by_death[next_death_ptr][1]
                except:
                    break

            if max_pop < current_pop:
                max_pop = current_pop
                max_pop_year = now

        return max_pop, max_pop_year

data = [[1987,2047],[1952,2006],[2021,2042],[2047,2049],[2036,2040],[1994,2009]]
test = Solution()
print(test.maximumPopulation(logs=data)) # not sure if this is absolutely wrong, but in terms of constraints it is wrong b/c it does not return the earliest year