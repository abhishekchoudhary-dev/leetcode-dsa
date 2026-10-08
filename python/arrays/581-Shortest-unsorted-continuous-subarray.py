# Problem: Leetcode 581 - Shortest unsorted continuous subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
# Time Complexity: O(n log n) as we are sorting
# Space Complexity: O(n) as we clone the array
# Approach: We simply compare array with its sorted version and find the start and end points till which we need to sort to 
# make the array sorted. the subarray between start and end will automatically come out to be the shortest


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        shortest = float('-inf')
        s = sorted(nums)
        if nums==s or len(nums)==1:
            return 0
        start = None
        end = 0
        for i in range(len(nums)):
            if nums[i]!=s[i]:
                if start is None:
                    start = i
                end = max(end,i)
                shortest = max(shortest,end-start+1)
        return shortest