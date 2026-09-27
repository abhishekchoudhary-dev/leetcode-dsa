# Problem: Leetcode 1190 - Remove substrings between each pair of parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-substrings-between-each-pair-of-parentheses/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we have to use a stack
# Approach: We simply keep appending to the stack and when when closing bracket is found we pop from stack till we find the opening bracket.
# since after popping the string between brackets is already reversed we just extend the stack with that string.
# The stack at the end of the loop holds the string elements with all brackets remove and string between brackets as reversed.
# Then we return a join of the array as a string

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char==')':
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop() #remove opening bracket
                stack.extend(temp)
            else:
                stack.append(char)
        return ''.join(stack)