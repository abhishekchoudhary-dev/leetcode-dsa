# Problem: Leetcode 1800 - Maximum ascending subarray sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) as we only use pointers
# Approach: We keep the current total and the best as the first element and each elemment that we find which forms 
# part of strictly increasing subarray we keep adding and keep taking the best and then
# if a smaller element is found and strictly increasing part is broken then total is reset to nums[i]

from typing import List
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        # can do brute force also which is O(n^3)
        # where we take all the subarrays and find the sum
        total = nums[0]
        best = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                total+=nums[i]
            else:
                total = nums[i]
            best = max(best,total)
        return best