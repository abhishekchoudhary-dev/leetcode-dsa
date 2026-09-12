# Problem: Leetcode 665 - Non decreasing array
# Difficulty: Medium
# Link: https://leetcode.com/problems/non-decreasing-array/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) 
# Approach: We have to sort the array so as soon as we find an element which is bigger than its next element
# we basically try to sort immediately. if element at i+1 is less than element at i-1 then we bump up the i+1 element to match element at i
# if i+1 is greater of equal to i-1 or i-1 does not exist then we just reduce the element at i to be equal to i+1.
# we can make a move and break and then compare the array to its sorted version and break. But this is slow.
# we rather keep track of moves used and if they go more than 1 we set a boolean flag which we move to False.
# and we break immediately to reduce iterations. then we return possible flag

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        moves=0
        possible = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if i>0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
                moves+=1
                if moves>1:
                    possible = False
                    break
        return possible