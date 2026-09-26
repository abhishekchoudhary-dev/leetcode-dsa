# Problem: Leetcode 3865 - Reverse k subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-k-subarrays/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: We calculate window size and keep cutting the subarrays and reverse and adding them to the answer

class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        ans = []
        window = len(nums)//k
        for i in range(0,len(nums)-window+1,window):
            sub = nums[i:i+window]
            ans.extend(sub[::-1])
        return ans
        