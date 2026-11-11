# Problem: Leetcode 325 - Maximum size subarray sum equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use as hashmap
# Approach: A very standard implementation of a hashmap based prefix sum with a sentinal value to start with
# addding sum 0 and index -1


class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        left = 0
        #hashmap prefix
        d = {0:-1}
        mx = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            if curr_sum - k in d:
                mx = max(mx,right-d[curr_sum-k])
            if curr_sum not in d:
                d[curr_sum]=right
        return mx