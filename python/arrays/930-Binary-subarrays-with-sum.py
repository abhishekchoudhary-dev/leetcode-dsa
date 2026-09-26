# Problem: Leetcode 930 - Binary subarrays with sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-subarrays-with-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(n) for hashmap
# Approach: We take a default dict and store 0 binary array with count 1 as 0 always exists
# then we keep incrementing the curr_bin sum to hashmap to show that their exists a subarray with curr_sum.
# since our target is 'goal' in every iteration i add d[curr_sum-goal] to the result that if there are any amounr of subarrays
# that have total of curr_sum - goal and those subarrays can all produce the sum of goal and we increment cnt by this amount
# finally we return count

from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cnt = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            cnt+=d[curr_sum-goal]
            d[curr_sum]+=1
        return cnt