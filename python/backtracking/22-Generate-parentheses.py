# Problem: Leetcode 22 - Generate parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/generate-parantheses/description/
# Time Complexity: O(n^2) as there is a nested recursive call for each call
# Space Complexity: O(n) as we keep a current string
# Approach: Use backtracking to generate all possible combination. we keep adding opening brackets. if opening brackets cross n 
# or closing brackets cross n or opening are less than closing we return immediately as a valid string cannot be found.
# otherwise if both are equal to n that means current string is valid and we are ready to append it.
# then we backtrack increasing each opening brackets and for each opening brackets we backtrack for each closing bracket also.
# at the end we return combinations.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def backtrack(left_count,right_count,current_string):
            if left_count>n or right_count>n or left_count < right_count:
                return
            if left_count == n and right_count==n:
                combinations.append(current_string[:])
                return
            backtrack(left_count+1, right_count,current_string+'(')
            backtrack(left_count,right_count+1,current_string+')')


        backtrack(0,0,'')
        return combinations