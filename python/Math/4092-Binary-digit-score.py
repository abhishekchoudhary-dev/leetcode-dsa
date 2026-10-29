#Problem: Leetcode 4092 - binary digit score
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-digit-score/description/
# Time Complexity: O(k) with k being the number of bits in the number
# Space Complexity: O(1) as no extra space is used
# Approach - We just find the set bits in both numbers and return the values as per the formulas provided 
# in the question


class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = a.bit_count()
        s2 = b.bit_count()
        if s1>=s2:
            return s1*s2
        return s2//s1