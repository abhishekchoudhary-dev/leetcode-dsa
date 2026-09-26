# Problem: Leetcode 3349 - Adjacent increasing subarrays detection
# Difficulty: Easy
# Link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-I/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space used
# Approach: Since input size is small we can brute force it by checking every starting point and slicing the two array with length of k each
# from that starting point and checking if both are strictly increasing. If yes we return True

from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        def is_strictly_increasing(arr):
            return all(arr[i]<arr[i+1] for i in range(len(arr)-1))
        #cannot use sorted as elements are repeating
        for i in range(len(nums)-2*k+1):
            first = nums[i:i+k] #check every starting point
            second = nums[i+k:i+2*k]
            if is_strictly_increasing(first) and is_strictly_increasing(second):
                return True
        return False