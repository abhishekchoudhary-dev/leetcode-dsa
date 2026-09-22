# Problem: Leetcode 643 - Maximum average subarray I
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-average-subarray-i/description/
# Time Complexity: O(n) as we iterate through the flowerbed once
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: Since we have to run a static size sliding window of size k we just quickly calculate the prefix sum at each index
# and then we run our window and keep calculating the average of each window and keeping a max variable.
# one thing to notice is that since average can be negative we keep max as -INF.

from typing import List

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        prefix = [0]*(len(nums)+1)
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            prefix[i+1] = curr_sum
        mx = float('-inf')
        window = k
        for i in range(len(nums)-window+1):
            mx = max(mx,(prefix[i+window]-prefix[i])/k)
        
        return mx