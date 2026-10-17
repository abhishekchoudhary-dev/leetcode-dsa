# Problem: Leetcode 2855 - Minimum right shifts to sort the array
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimun-right-shifts-to-sort-the-array/description/
# Time Complexity: O(n^2) for slicing approach and O(n) for normal approach
# Space Complexity: O(n) for approach2 and O(1) for normal approach
# Approach1: we simply check the number of drops which should only be 1 if array can be rotates and sorted
# if its more than 1 we return -1 and if 0 we return 0 and otherwise we return length of array - rotation index

from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        unsorted = 0
        rotateIdx = 0
        for i,num in enumerate(nums):
            if nums[i] > nums[(i+1)%len(nums)]:
                unsorted+=1
                rotateIdx = i+1
        if not unsorted:
            return 0
        if unsorted>1: return -1
        return len(nums) - rotateIdx

        '''
        s = sorted(nums)
        n = len(nums)
        if nums == s:
            return 0
        for i in range(1,len(nums)):
            if nums[i:] + nums[:i] == s:
                return n-i
        return -1
        '''