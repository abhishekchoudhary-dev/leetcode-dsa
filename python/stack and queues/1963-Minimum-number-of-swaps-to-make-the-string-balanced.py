# Problem: Leetcode 1963 - Minimum number of swaps to make the string balanced
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a stack
# Approach: We only append the open brackets and when closing bracket is found if stack exsits
# then ofcourse we will have something in the stack to match with always so we pop it
# otherwise we keep unbalanced count. At the end we do (unabalanced+1)//2 as each operation of swap
# fixes 2 closing brackets so we have to use for x+k-1//2. 

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unbalanced = 0
        for bracket in s:
            if bracket=='[':
                stack.append(bracket)
            else:
                if stack: #i am only adding opening ones
                    stack.pop()
                else:
                    unbalanced+=1
        if not stack:
            return 0
        return (unbalanced+1)//2