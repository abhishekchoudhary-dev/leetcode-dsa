# Problem: Leetcode 974 - Subarray sums divisible by k
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: We keep storing how many times a particular remainder has been seen by incrementing its count.
# and then for each iteration we will add to result the hashmap value of curr_sum%k as those are the number of subarrays
# which will combine with current element to make a subarray with sum which is divisible by k


from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            res+=d[curr_sum%k]
            d[curr_sum%k]+=1
        return res