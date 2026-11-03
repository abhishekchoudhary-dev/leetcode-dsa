# Problem: Leetcode 4097 - Minimum value of merged integers
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-value-of-merged-integers/description/
# Time Complexity: O(k) with k being digits as we concatenate each pair with total k digits
# Space Complexity: O(1) as we do not use extra space
# Approach: Straighfotward question we keep jumping index with 2 and concatenating two integerss and comparing the value with 
# the running maximum

class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        mn = float('inf')
        for i in range(0,len(nums)-1,2):
            value = int(str(nums[i]) + str(nums[i+1]))
            mn = min(mn,value)
        return mn