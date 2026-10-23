
# Problem: Leetcode 3644 - Maximum k to sort a permutation
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
# Approach: Main idea is to figure out which elements need to be moved and finding their common set bit. Only is 
# all the elements have a common set bit can their be a k which will be result of their AND.
# as only that bit will figure in the and operation as every other alternating bits go to zero


from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        s  = sorted(nums)
        k = None
       
        for i in range(len(nums)):
            if nums[i]!=s[i]:  
                if k is None:
                    k = nums[i]
                k&=nums[i]
        return k if k else 0