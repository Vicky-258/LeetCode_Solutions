class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        upper, lower = 2 ** 31 - 1, -2 ** 31

        if num > upper:

            num = upper

        elif num < lower:

            num = lower

        return num