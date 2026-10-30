# Problem: Leetcode 1403 - Minimum subsequence in non increasing order
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/
# Time Complexity: O(n log n) as we have to sort the array multiple times for reversing
# Space Complexity: O(1) as no extra data structure used
# Approach: The requirement are complicated but main idea is to realize that since we have to return the smallest length of all possible subsequences 
# which will have sum greater than remaining then it can only include the bigger numbers. So we just reverse sort the array
# and loop on it to find the index where we should cut as soon as sum exceeds sum from the remaining elements.
# then we cut it and return that first part of reversed array


class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        cut = 0
        curr_sum = 0
        for i,num in enumerate(nums):
            curr_sum+=num
            if curr_sum > s - curr_sum:
                cut = i
                break
        return sorted(nums[0:i+1], reverse=True)