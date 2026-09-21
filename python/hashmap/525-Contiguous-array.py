# Problem: Leetcode 525 - Contiguous array
# Difficulty: Medium
# Link: https://leetcode.com/problems/contiguous-array/description/
# Time Complexity: O(n) as we go through the array once
# Space Complexity: O(n) as we use a hashmap
# Approach: We keep recording the difference of ones and zero seen at each index and if there are two indices
# where the diff is equal it means the subarray between those indices has equal number of ones and zeros
# If diff is found in hashmap then we update our max variable. otherwise we only add diff to hashmap if its not in the hashmap
# so that we always keep the initial value and avoid overwriting the index so that we always find the longest hashmap

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = zeros = 0
        d = {0:-1}
        mx = 0
        for i,num in enumerate(nums):
            if num == 1:
                ones+=1
            else:
                zeros+=1
            diff = ones - zeros
            if diff in d:
                mx = max(mx,i-d[diff])
            else:
                d[diff] = i
        return mx