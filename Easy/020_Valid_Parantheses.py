class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for ch in s:

            if ch in brackets:

                stack.append(ch)

            elif stack and ch == brackets[stack[-1]]:

                stack.pop()

            else:

                return False

        if stack:
            return False
        else:
            return True

