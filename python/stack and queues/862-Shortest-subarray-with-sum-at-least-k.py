# Problem: Leetcode 862 - Shortest subarray with sum at least k
# Difficulty: Hard
# Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we have a deque
# Approach: We maintain a monotonic deque which keep all the indices. Then on the prefix sum calculated for every index
# we iterate and check if any indices from beginning of deque can make a subarray with sum >= k.
# If yes we keep popping and keep taking the min length. then one length is taken before appending the index we check if 
# there are already indices which have prefix_sum greater than sum at current_idx then we just delete them and 
# as any future index will be able to make a smaller subarray and in a way it also mean that curr_sum has decreased if its less
# than prefix_sum[q[-1]] meaning a negative element was encountered.


from collections import deque
from typing import List
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        mn = float('inf')
        curr_sum = 0
        prefix_sum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i] #can acccumulate

        q = deque()
        for idx,curr_sum in enumerate(prefix_sum):
            while q and curr_sum - prefix_sum[q[0]]>=k:
                mn = min(mn, idx - q[0])
                q.popleft()
            #monotonic
            while q and prefix_sum[q[-1]] >= curr_sum: #as numbers can be negative
                q.pop()

            q.append(idx)
        return -1 if mn==float('inf') else mn