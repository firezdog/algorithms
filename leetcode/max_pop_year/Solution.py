from typing import List


'''
This finally works, based off answer in one of the comments on the original problem.
That solution flattens the original data into a list of years and pop changes for that year --
Somewhat similar to my original idea that there's an isomorphism of a kind between this problem
and finding the earliest max open parentheses in a string.  
I found it necessary to use a dictionary first 
because the original flattened event_list could contain duplicate years and return an incorrect maximum
based on a partial population update for that year.
'''
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for birth_year, death_year in logs:
            events.append([birth_year, 1])
            events.append([death_year, -1])
        
        events = sorted(events, key=lambda event: event[0])

        current_pop = 0
        max_pop = [0,0]

        idx = 0
        while idx < len(events):
            event = events[idx]
            year = event[0]
            result = event[1]

            current_pop += result

            if (
                max_pop[0] < current_pop 
                and idx + 1 < len(events) 
                and not events[idx +1][0] == year
            ):
                max_pop[0] = current_pop
                max_pop[1] = year
        
            idx += 1
        
        return max_pop[1]