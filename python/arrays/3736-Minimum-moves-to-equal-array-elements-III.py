# Problem: Leetcode 3736 - Maximum moves to equal array elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
# Time Complexity: O(n) - find max and then compare each element with it
# Space Complexity: O(1)
# Approach: Since each element is individual now each one's distance needs to be compared with the maximum element
# and then the total has to be calculated by diff of each element with the maximum value

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        return sum(mx-nums[i] for i in range(len(nums)))