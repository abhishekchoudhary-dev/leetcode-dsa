# Problem: Leetcode 462 - Minimum moves to equal array elements II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space used
# Approach: We can brute force by trying every value but that would probably TLE so the idea is to realize for which there is always mathematical proof
# that the minimum distance will be from the median to each value.  to find he median we have to sort the array
# and then we take the median value.

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = len(nums)//2 #if len(nums)%2==0 else (len(nums)-1)//2
        moves = 0
        for num in nums:
            moves+=abs(num-nums[median])
        return moves