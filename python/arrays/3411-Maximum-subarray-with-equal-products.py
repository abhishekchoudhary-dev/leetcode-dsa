# Problem: Leetcode 3411 - Maximum subarray with equal products
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-subarray-with-equal-products/description/
# Time Complexity: O(n^2) + prefix to avoid an O(n^3) loop
# Space Complexity: O(n) as we calculate prefix sums
# Approach: We have to calculate the lcm and gcd of each subarray so to avoid O(n^3) loop we calculate the product of the subarray
# by precalculating the prefix product and then we can calcutate the product in O(1) time and gcd and lcm are calulated using in build functions.
# then we keep updating our best variable to hold the best possible answer. 

from typing import List
import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        best = 0
        prefix = [0]*(len(nums)+1)
        prod = 1
        for i in range(len(nums)):
            prod*=nums[i]
            prefix[i+1] = prod

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub = nums[i:j+1]
                g = math.gcd(*sub)
                l = math.lcm(*sub)
                p = (prefix[j+1]//prefix[i] if prefix[i]!=0 else prefix[j+1] - prefix[i])
                if p == l*g:
                    best = max(best,j-i+1)
        return best