from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        left = 0
        have = Counter()
        length = len(p)
        res = []
        matches = 0

        for right in range(len(s)):
            char = s[right]

            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    matches += 1
                elif have[char] == need[char] + 1:
                    matches -= 1

            if right - left + 1 > length:
                remove_char = s[left]
                left += 1

                if remove_char in need:
                    if have[remove_char] == need[remove_char]:
                        matches -= 1
                    have[remove_char] -= 1
                    if have[remove_char] == need[remove_char]:
                        matches += 1

            if matches == len(need):
                res.append(left)

        return res
