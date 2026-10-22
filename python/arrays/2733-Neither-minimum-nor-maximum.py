# Problem: Leetcode 2733 - Neither Minimum nor maximum
# Difficulty: Easy
# Link: https://leetcode.com/problems/neither-minimum-nor-maximum/description/
# Time Complexity: O(n log n) as we sort the array
# Space Complexity: O(1) as no extra data structure is used
# Approach: We simply sort the array so we have min and max and then loop the array and as soon as we find an element
# which is smaller than both we just return it


from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)-1):
            if nums[i] > nums[0] and nums[i] < nums[-1]:
                return nums[i]
        return -1