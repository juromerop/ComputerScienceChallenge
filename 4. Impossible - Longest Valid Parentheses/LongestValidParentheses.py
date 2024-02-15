class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest =0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                elif len(stack) != 0:
                    longest = max(longest, i-stack[-1])
        return longest