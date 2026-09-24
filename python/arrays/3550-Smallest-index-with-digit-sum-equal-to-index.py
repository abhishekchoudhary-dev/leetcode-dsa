# Problem: Leetcode 3550 - Smallest index with digit sum equal to index
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We simply loop and check each value if its digit sum is equal to current index.
# If yes then we immediately return since we have to return the smallest index
from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = sum(int(d) for d in str(nums[i]))
            if s==i:
                return i
        return -1