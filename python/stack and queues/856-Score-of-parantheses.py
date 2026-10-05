# Problem: Leetcode 856 - Score of parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/score-of-parantheses/description/
# Time Complexity: O(n)
# Space Complexity: O(1) for balance approach and O(n) for stack
# Approach1: We just maintain the depth that we are in and if we find complete valid bracket with 0 depth
# we add 2 to the power 0 to result which is one and correct, and if there is depth it will account for in the formula 2**depth.
# So everytime we find closing bracket we check if the bracket just before is opening and if yes then we add to score based on current depth we are at
# if its not opening means we are just coming out of the depth without adding to score.
# Approach2: we use a stack to actually keep track of the score which we can imagine in the sense of depth
# on opening bracket we append 0 and on closing we pop the top of stack and then change the top 
# of stack element as max of 2*last popped leemnet or 1 meaning that if last popped was 0 then now last element would be 1 meaning we 
# were at 0 depth and now we are at 1 else 2*v will always be higher and then depth will be added to stack
# the element left in stack at the end will be the answer.



class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal = 0
        score = 0
        for i,char in enumerate(s):
            if char=='(':
                bal+=1
            else:
                bal-=1
                if s[i-1]=='(':
                    score+=2**bal
        return score

        '''
        stack = [0]
        score = 0
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                #balanced string is guaranteed
                v = stack.pop()
                stack[-1]+=max(2*v,1)
        return stack.pop()
        '''