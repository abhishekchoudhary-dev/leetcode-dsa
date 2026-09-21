# Problem: Leetcode 540 - Single element in sorted array
# Difficulty: Medium
# Link: https://leetcode.com/problems/single-element-in-sorted-array/description/
# Time Complexity: O(n log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We do binary search on indices as each pairs should have first number on even index and second on odd index.
# if mid is odd we just decrement it to check pair and if pair matches then we move left to 2 as the possible number is on the right of it
# oherwise we set right to mid to not rule out mid as a possible answer

from typing import List 

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #try for O(log n)
        lo , hi = 0, len(nums)-1
        while lo<hi:
            mid = (lo+hi)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                lo = mid+2
            else:
                hi = mid
        return nums[hi] #hi and lo both converge to answer


        '''
        #O(n) solution
        xor = 0
        for num in nums:
            xor^=num
        return xor
        '''
        