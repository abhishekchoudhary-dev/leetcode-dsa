 
# Problem: Leetcode 2027 - Minimum moves to convert string
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-moves-to-convert-string/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We need to optimize by not unnecessarily checking every group of 3 elements but rather only changin them when 
# the current element is X as at that moment we have to change it to O and then we jump our index 3 places
# as the next 3 element have already be changed top 'O' and we dont want to waste a move.


class Solution:
    def minimumMoves(self, s: str) -> int:
        if 'X' not in s:
            return 0
        ops = 0
        i = 0
        while i < len(s):
            if s[i]=='X': #to be optimal i only apply when start is X so i cannot avoid
                ops+=1
                i+=3
                continue
            i+=1
        return ops