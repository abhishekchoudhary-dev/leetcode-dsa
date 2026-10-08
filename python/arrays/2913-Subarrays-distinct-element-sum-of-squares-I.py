# Problem: Leetcode 2913 - Subarrays distinct element sum of squares I
# Difficulty: Easy
# Link: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-I/description/
# Time Complexity: O(n^2) - as we go through the nested loop
# Space Complexity: O(n) as we make a subarray
# Approach1: Since constraints are small we just check in nested loop each subarray and take the square of 
# the number of unique elements and add that in the total. Since the unique elements in not a monotonic property, 
# hence we are not able to use prefix sums.

from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        #pre compute list elements
        total = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub = nums[i:j+1]
                total+=len(set(sub))**2

        return total