
# Problem: Leetcode 2221 - Find triangular sum of array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-triangular-sum-of-array/description/
# Time Complexity: O(n) for n elements in nums
# Space Complexity: O(1) as no extra data structure is used
# Approach: We simply follow what the questions asks where we keep assigng the values to newNums as per given formula and 
# keep reassigning newNums to nums

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums)!=1:
            newNums = [0]*(len(nums)-1)
            for i in range(len(nums)-1):
                newNums[i] = (nums[i] + nums[i+1])%10
            
            nums = newNums
        
        return nums[0]