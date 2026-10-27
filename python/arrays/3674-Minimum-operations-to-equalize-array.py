
# Problem: Leetcode 3674 - Maximum operations to equalize array
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-operations-to-equalize-array/description/
# Time Complexity: O(n) due to set conversion
# Space Complexity: O(1)
# Approach: Since we are allowed to do AND of the entire array then ofcourse in one operation we can definitely 
# do this and and replace all elements with this AND. so its always possible to do it in one operation
# but only in case we have array already sorted then we need 0 operations.

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        return 1