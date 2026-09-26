# Problem: Leetcode 1708 - Largest subarray length k
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-subarray-length-k/description/
# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: Since we need to find the largest subarray with length k and largest is defined with an unequal element at an index being bigger
# we just too till len(nums)-k and find the largest starting element as that will guarantee the largest subarray.
# once we find the largest element we return the slicing subarray of length k from that point on.

class Solution:
    def largestSubarray(self, nums: list[int], k: int) -> list[int]:
        if k ==1:
            return [max(nums)]
        mx = 0
        target = 0
        #cannot enumerate this time as input size is big
        #find best starting point
        for i in range(len(nums)-k+1):
            if nums[i] > mx:
                mx = nums[i]
                target = i
            
        return nums[target:target+k] # return the subarray