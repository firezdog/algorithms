import operator

def solution(S: str):
    vc = VowelCounter(sentence=S)
    return vc.solution


class VowelCounter:
    """Given a sentence, generates a dictionary with counts for each vowel in the sentence and a string listing the vowel(s) that occurred most frequently"""
    def __init__(self, sentence: str):
        self._vowel_counts: dict[str, int] = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        self._sentence: str = sentence.lower()
        self._count_vowels()
        self._solution: str = self._find_solution()

    def _count_vowels(self):
        # Update the dictionary to reflect the given sentence.
        for char in self._sentence:
            count: int = self._vowel_counts.get(char)
            if count is not None:
                self._vowel_counts[char] = count + 1
    
    def _find_solution(self) -> str:
        # Sort the dictionary of vowels by frequency (highest to lowest) and generate a string listing all tied entries.
        sorted_vowel_counts: List[Tuple[str, int]] = sorted(
            self._vowel_counts.items(), 
            key=operator.itemgetter(1), 
            reverse=True
        )

        solution_string = ''
        max_vowel_count = sorted_vowel_counts[0][1]   # ties have the same as the first item in the sorted list
        for vowel, vowel_count in sorted_vowel_counts:
            if vowel_count != max_vowel_count:
                break   # stop once we get past the ties
            time_declension = 'times' if vowel_count > 1 else 'time'   # determine whether 'time' is plural
            solution_string += f'{vowel} appears {vowel_count} {time_declension}\n'
        return solution_string[:-1] # return the answer except for the last \n
    
    @property
    def solution(self):
        return self._solution