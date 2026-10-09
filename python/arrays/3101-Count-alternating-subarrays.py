# Problem: Leetcode 3101 - Count alternating subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-alternating-subarrays/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We simply find subarrays that are alternating and we know that the number of subarrays of a subarray of length n lets says
# is n*(n+1)/2 and this way we add to our count. if j is greater than i then we make i = j+1 else we make j++

from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        while i < len(nums):
            j = i
            while j+1<len(nums) and nums[j]!=nums[j+1]:
                j+=1
            l = j-i+1
            cnt += l*(l+1)//2
            i = (j+1 if j>i else i+1)
        return cnt
            