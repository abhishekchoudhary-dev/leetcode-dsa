# Problem: Leetcode 1111 - Maximum nesting depth of two valid parantheses strings
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parantheses-strings/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we have to use a stack
# Approach: Main appraoch uses a manual stack and depth tracking approach where we append to that stack which we find to have less depth
# and also pop from the one which has more depth. But faster approach is to divide the parantheses into group of 0 and 1 since the 
# while parantheses string is guaranteed to be valid. So we keep adding to the different groups and the parity will automatically add to alternative groups 
# and also same for closing bracket and in this case we dont have to pop anything

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        #group based paranthesis assignment
        depth = 0
        ans = []
        for char in seq:
            if char == '(':
                depth+=1
                ans.append(depth%2)
            elif char == ')':
                ans.append(depth%2)
                depth-=1
        return ans
        '''
        original solution - O(n)
        ans = []
        stackA = []
        stackB = []
        depthA = depthB = 0
        for i,char in enumerate(seq):
            if char=="(":
                if (stackA and stackA[-1]==')') or not stackA:
                    stackA.append(char)
                    depthA+=1
                    ans.append(0)
                else:
                    #if stackA open or stack B also open then we check depth
                    if not stackB:
                        stackB.append(char)
                        ans.append(1)
                        depthB+=1
                    elif stackA and stackA[-1]=='(' and stackB and stackB[-1]=='(':
                        if depthA>=depthB:
                            stackB.append(char)
                            depthB+=1
                            ans.append(1)
                        else:
                            stackA.append(char)
                            depthA+=1
                            ans.append(0)
                        
            else:
                if (stackA and stackA[-1]=='(') and (stackB and stackB[-1]=='('):
                    if depthA >= depthB:
                        stackA.pop()
                        depthA-=1
                        ans.append(0)
                    else:
                        stackB.pop()
                        depthB-=1
                        ans.append(1)
                elif stackA and stackA[-1]=='(':
                    stackA.pop()
                    depthA-=1
                    ans.append(0)
                elif stackB and stackB[-1]=='(':
                    stackB.pop()
                    depthB-=1
                    ans.append(1)
        return ans
        '''
             