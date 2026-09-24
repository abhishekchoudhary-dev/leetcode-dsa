# Problem: Leetcode 3452 - Sum of good numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-good-numbers/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We take each number and check if i-k and i+k are in range for it and take it if its strictly greater than both in the range
# or greater than one of them in the range and if yes then we include it in the total.


from typing import List
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)
        for i in range(len(nums)):
            if i-k<0 and i+k>(n-1):
                total+=nums[i]
            else:
                if (i-k>=0 and i+k<n) and nums[i]> nums[i-k] and nums[i] > nums[i+k]:
                    total+=nums[i]
                elif i-k>=0 and i+k>(n-1) and nums[i] > nums[i-k]:
                    total+=nums[i]
                elif i-k<0 and i+k<n and nums[i] > nums[i+k]:
                    total+=nums[i]
                    
        return total