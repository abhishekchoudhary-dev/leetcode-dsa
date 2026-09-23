# Problem: Leetcode 1658 - Minimum operatiosn to reduce x to zero
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
# Time Complexity: O(n) due to single pass through the array.
# Space Complexity: O(n) as we use a prefix sum hashmap
# Approach: We can transform the question into a sliding window problem by finding a target by doing sum(nums)-x
# because if we find a window with sum equal to target then the reamining elements on left and right of the window can be removed
# and then those removed elements will be enough to reduce x to zero. Therefore we run a sliding window and we find occurence of target.
# important is to realize that we need to find the largest such window because we intednd to remove the least number of such elements
# So we keep updating length in with max and at the end we return the len(nums)- window length as that is the amount of elements we need to remove.

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        d = {0:-1}
        curr_sum = 0
        target = sum(nums) - x
        if target==0:
            return len(nums)
        length = float('-inf')
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum - target in d:
                length = max(length,i - d[curr_sum - target])
            d[curr_sum] = i # since positive values curr_sum will not repeat
        return len(nums) - length if length!=float('-inf') else -1