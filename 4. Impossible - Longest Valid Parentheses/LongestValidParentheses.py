'''
My solution to the problem uses a stack to keep track of the indices of the parentheses.
I iterate through the string and when I find an open parenthesis, I add its index to the stack.
When I find a close parenthesis, I pop the last element from the stack and calculate the length of the valid parentheses.
I keep track of the longest valid parentheses and return it at the end.
'''
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