# Problem: Leetcode 713 - Subarray product less than k
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-product-less-than-k/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We run a simple sliding window and we keep counting arrays by the idea of right - left+1 which counts
# how many subarrays end at right index.When right moves further then all subararys will automatically be unique
# as now there is a new ending point.

from collections import defaultdict
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        #tarditional window
        cnt = 0
        left = 0
        curr_prod = 1
        for right in range(len(nums)):
            curr_prod*=nums[right]
            while left <= right and curr_prod >= k:
                curr_prod /= nums[left]
                left+=1
            cnt += right-left+1
            
        return cnt