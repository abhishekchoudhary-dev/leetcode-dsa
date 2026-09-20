# Problem: Leetcode 439 - Ternary expression parser
# Difficulty: Medium
# Link: https://leetcode.com/problems/ternary-expression-parser/description/
# Time Complexity: O(n) for stack based approches and O(n^2) for RPN and window approach
# Space Complexity: O(n) as we use a stack or we slice windows
# Approach: Multiple approaches have been discussed including the stack based, RPN based and the window based where each window from right to left is checked and evaluated before moving further
# Stack based appraoch finds O(n) solution where we resolve an expression from the right side as soon as it is found. We add everything to stack and pop values when a '?' is found
# and then we return top of stack at the end which will have just one element.

class Solution:
    def parseTernary(self, expression: str) -> str:
        #Another stack based approach - O(n)
        stack = []
        for e in expression[::-1]:
            if stack and stack[-1]=='?':
                stack.pop() #remove ?
                first = stack.pop()
                stack.pop() #remove :
                second = stack.pop()
                stack.append(first if e == 'T' else second)
            else:
                stack.append(e)
        return stack[0]
        '''
        # stack based O(n) - push limited things
        stack = []
        i = len(expression)-1
        while i>=0:
            char = expression[i]
            if char in 'TF0123456789':
                stack.append(char)
            elif char=='?':
                #always pop both
                first = stack.pop()
                second = stack.pop()
                if expression[i-1]=='T':
                    stack.append(first)
                elif expression[i-1]=='F':
                    stack.append(second)
                i-=1
            i-=1
        return stack[0]
        '''


        '''
        #Approach2 - RPN based this is O(n^2)
        while len(expression)!=1:
            questionMarkIndex = len(expression)-1
            while expression[questionMarkIndex] != '?':
                questionMarkIndex-=1
            if expression[questionMarkIndex-1] == 'T':
                value = expression[questionMarkIndex+1]
            else:
                value = expression[questionMarkIndex+3]
            expression = expression[:questionMarkIndex-1] + value + expression[questionMarkIndex+4:]
        
        return expression
        '''
        
        '''
        This is O(n^2) - window based approach
        def isValidWindow(e: list)->bool:
            if (e[0] not in ('T','F')) or (e[1]!='?') or (e[2] not in 'TF0123456789') or (e[3]!= ':') or (e[4] not in 'TF0123456789'):
                return False
            return True

        def evalWindow(e: list)->str:
            return e[2] if e[0]=='T' else e[4]
        #right to left
        while len(expression)!=1:
            j = len(expression)-1
            while not isValidWindow(expression[j-4:j+1]):
                j-=1
            expression = expression[:j-4]+evalWindow(expression[j-4:j+1]) + expression[j+1:]
        
        return expression
        '''