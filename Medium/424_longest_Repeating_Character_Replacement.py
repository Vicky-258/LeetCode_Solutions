from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_freq = 0
        freq = defaultdict(int)
        len_sub = 0

        for right in range(len(s)):

            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            while right - left + 1 - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            len_sub = max(len_sub, right - left + 1)

        return len_sub
