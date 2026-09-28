# Problem: Leetcode 3105 - Longest strictly increasing or strictly decreasing subarray
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
# Time Complexity: O(n) for usual approach and O(n^3) for second brute force approach
# Space Complexity: O(1)
# Approach: Brute force approach below is straightforward where we take each substring and then check if its strictly increasing or not and take its length
# which become O(n^3) complexity quickly. So we use O(n) appraoch where we count the inc and dec
# and best are set to 1 and we count the longest inc or dec sequence and if there is something else 
# and then we reset the other to 1 and keep taking the incrementing inc or dec and keeping updating the best variable


from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = inc = dec = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = 1
                dec+=1
            elif nums[i]<nums[i+1]:
                inc+=1
                dec=1
            else:
                inc = 1
                dec = 1
            best = max(best,inc,dec)
        return best
        '''
        brute force
        def is_strictly(arr):
            return all(arr[i]<arr[i+1] for i in range(len(arr)-1)) or all(arr[i]>arr[i+1] for i in range(len(arr)-1))
        best = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub = nums[i:j+1]
                if is_strictly(sub):
                    best = max(best,len(sub))
        return best
        '''