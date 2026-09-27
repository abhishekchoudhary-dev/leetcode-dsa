# Problem: Leetcode 4065 - Rearrange array by removing distinct values
# Difficulty: Easy
# Link: https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/description
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We take freq in a hashmap and then keep adding them to answer while decrement key values by 1 each after appending it to ans array
# and if ans array length reachs length of nums then we just return answer.

from collections import Counter
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        nums.sort()
        d = Counter(nums)
        while len(ans)<len(nums):
            for key in d.keys():
                if d[key]>0:
                    ans.append(key)
                    d[key]-=1
        return ans