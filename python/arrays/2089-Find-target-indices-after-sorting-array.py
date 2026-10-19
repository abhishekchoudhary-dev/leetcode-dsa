# Problem: Leetcode 2089 - Find target indices after sorting array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
# Approach: Straightforward question to sort and collect indices where element is target

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        s = sorted(nums)
        return [idx for idx in range(len(s)) if s[idx]==target]