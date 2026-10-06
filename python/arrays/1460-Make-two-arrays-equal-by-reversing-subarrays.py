# Problem: Leetcode 1460 - Make two arrays equal by reversing subarrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) depending on what type of internal sort is used
# Approach: Since all types of swapping is allowed we basically have to check parity of starting and target array.
# If they have equal parity then we can say that target can be achieved since any pair can be shuffled.


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(arr)==sorted(target)