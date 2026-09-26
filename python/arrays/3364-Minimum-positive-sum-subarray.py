# Problem: Leetcode 3364 - Minimum positive sum subarray
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-positive-sum-subarray/description/
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Approach: Since input size is small we enumerate all subarrays with help of two pointers
# and then we check if the sum of this subarray >0 and if yes we update our best value. At the end
# we check if update has been set then we return it else we return -1


from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        best = float('inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j-i+1>=l and j-i+1<=r:
                    s = sum(nums[i:j+1])
                    if s>0:
                        best = min(best,s)
        return best if best!=float('inf') else -1