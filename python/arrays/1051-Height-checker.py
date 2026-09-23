# Problem: Leetcode 1051 - Height checker
# Difficulty: Easy
# Link: https://leetcode.com/problems/height-checker/description/
# Time Complexity: O(n log n)
# Space Complexity: O(n) as we stored sorted list
# Approach: We basically have to check how many people are not at their right positions.
# so we sort the array and in a generator expression we check if they are not at their correct position and add 1 for each.

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        s = sorted(heights)
        return sum(1 for i,height in enumerate(heights) if height!=s[i])