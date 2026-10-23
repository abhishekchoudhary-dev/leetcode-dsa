# Problem: Leetcode 2869 - Minimum operations to collect elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimun-operations-to-collect-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(n) for the answer array
# Approach: We simply loops backwards and keep collecting if elements is less than k and we keep collection as a set
# to ignore duplicates. Then if the length of s reaches k it means every element has been collected
# so we break and return the operations

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = set()
        ops = 0
        for num in nums[::-1]:
            ops+=1
            if num<=k:
                collection.add(num)
                if len(collection) == k:
                    break
        return ops