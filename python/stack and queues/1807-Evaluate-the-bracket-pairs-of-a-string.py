# Problem: Leetcode 1807 - Evaluate the bracket pairs of a string
# Difficulty: Medium
# Link: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a stack
# Approach: We iterate and keep adding elements to stack. If a closing bracket is found, then we pop till we find the opening bracket
# and they reverse the key within brackets,look up its meaniing in our hashmap and extend our stack with the meaning and then keep appending 
# the normal elements. This way we build the stack with meanings replace for elements in brackets and we can just 
# join the stack into a string and return it

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        for pair in knowledge:
            name,meaning = pair
            d[name] = meaning
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop() #remove opening bracket
                key = ''.join(temp[::-1])
                if key in d:
                    stack.extend(d[''.join(temp[::-1])])
                else:
                    stack.extend('?')
            else:
                stack.append(char)
        return ''.join(stack)
        