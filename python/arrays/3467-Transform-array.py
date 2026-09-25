# Problem: Leetcode 3467 - Transform array
# Difficulty: Easy
# Link: https://leetcode.com/problems/transform-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: Simple question where we make changes as per the requirement in the array. We are building new array but we can also make changes in place
# with an index.

from typing import List
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = [0 if nums[i]%2==0 else 1 for i in range(len(nums))]
        res.sort()
        return res