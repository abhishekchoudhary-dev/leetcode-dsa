# Problem: Leetcode 32 - Longest valid parentheses
# Difficulty: Hard
# Link: https://leetcode.com/problems/longest-valid-parentheses/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a stack to push and pop elements
# Approach: We start with valid stack starting at -1 to deal with first element being closing bracket which is then pooped
# and 0 index is added. basically the index added is of the invalid parentheses list where the last invalid streak end
# so that we can subtract it from valid one and get the length of the valid string
# when we find open brakcet we keep appending the index and when we find closing bracket we pop the last index and check if stack is empty
# if yes we append current index as that means everything upto current index that was valid was already seen.



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        bracket_stack = [-1] #baseline
        max_length = 0
        length = 0
        for index in range(len(s)):
            if s[index] == '(':
                bracket_stack.append(index)
            else:
                bracket_stack.pop()
                if not bracket_stack:
                    bracket_stack.append(index)
                else:
                    max_length = max(max_length, index - bracket_stack[-1])
                

        return max_length