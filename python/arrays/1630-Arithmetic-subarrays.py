# Problem: Leetcode 1630 - Arithmetic subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/arithmetic-subarrays/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we slice subarrays
# Approach: We slice subarrays as per l and r index values and check if they all differences between them after sorting to be equal.
# if they do then that means that it is arithmetic subarray and we update ans[i] to True


class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ans = [False] * len(l)
        def check(arr):
            arr.sort()
            return len(set([arr[i]-arr[i-1] for i in range(1,len(arr))]))==1
        for i in range(len(l)):
            sub = nums[l[i]:r[i]+1]
            if check(sub):
                ans[i] = True
        return ans