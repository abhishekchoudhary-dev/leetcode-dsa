# Problem: Leetcode 20 - Valid parantheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parantheses/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a stack to push and pop elements
# Approach: We simply keep adding to stack if its an opening bracket and if its closing bracket
# we check the last element of stack to see that it should be the matching opening bracket of the closing bracket
# and then if its not we immediately return False or else we pop from stack. at the end we check if len(stack)==0
# if it is we just return true else false.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c=='{' or c=='[':
                stack.append(c)
            if c==')' or c=='}' or c==']':
                if not stack or (c==')' and stack[-1]!='(') or (c==']' and stack[-1]!='[') or (c=='}' and stack[-1]!='{'):
                    return False
                stack.pop()
        return len(stack)==0

        '''
        bracket_stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                bracket_stack.append(char)
                continue
            if char ==')':
                if not bracket_stack:
                    return False
                last_element = bracket_stack.pop()
                if last_element != '(':
                    return False
            if char == '}':
                if not bracket_stack:
                    return False
                last_element = bracket_stack.pop()
                if last_element != '{':
                    return False
            if char ==']':
                if not bracket_stack:
                    return False
                last_element = bracket_stack.pop()
                if last_element != '[':
                    return False
            
        
        return len(bracket_stack) == 0
        '''