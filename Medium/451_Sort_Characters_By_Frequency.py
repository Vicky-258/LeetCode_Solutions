from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)

        freq = {key : value for key, value in sorted(freq.items(), key = lambda ele : ele[1], reverse=True)}

        res = ""

        for key, value in freq.items():
            res += key*value

        return res
