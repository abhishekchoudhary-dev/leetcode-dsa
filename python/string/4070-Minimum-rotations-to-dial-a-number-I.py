
#Problem: Leetcode 4070 - Minimum rotations to dial a number I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-rotations-to-dial-a-number-I/description/
# Time Complexity: O(n) - as we iterate on words
# Space Complexity: O(1)
# Approach: We simply at each step take the minimum step from current prev number to current either clockwise
# or anticlockwise 10 - val. 


class Solution:
    def minRotations(self, s: str) -> int:
        rot = min(abs(int(s[0])-0),10-abs(int(s[0])-0))
    
        for i,digit in enumerate(s[1:],1):
            val = abs(int(digit)-int(s[i-1]))
            rot+= min(val,10-val)
        return rot