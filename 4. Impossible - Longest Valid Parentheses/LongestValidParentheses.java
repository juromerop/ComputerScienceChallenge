/*
My solution to the problem uses a stack to keep track of the indices of the parentheses.
I iterate through the string and when I find an open parenthesis, I add its index to the stack.
When I find a close parenthesis, I pop the last element from the stack and calculate the length of the valid parentheses.
I keep track of the longest valid parentheses and return it at the end.
 */
import java.util.Stack;

class   {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int longest = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    longest = Math.max(longest, i - stack.peek());
                }
            }
        }
        return longest;
    }
}
