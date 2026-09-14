# Problem: Leetcode 961 - N repeated element in size 2N array
# Difficulty: Easy
# Link: https://leetcode.com/problems/N-repeated-element-in-size-2N-array/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: As only one element repeats we only have to return the first duplicate found which is quite straightforward.
# so we keep a set and if an element found in the set we return it immediately.


from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)