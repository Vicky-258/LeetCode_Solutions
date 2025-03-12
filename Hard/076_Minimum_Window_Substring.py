from collections import defaultdict, Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        left = 0
        need = Counter(t)
        have = defaultdict(int)
        have_count = 0

        res, res_len = "", float("inf")

        for right in range(len(s)):
            char = s[right]

            have[char] += 1

            if have[char] == need[char]:
                have_count += 1

            while have_count == len(need):

                if right - left + 1 < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    have_count -= 1
                left += 1

        return res if res_len != float("inf") else ""