# Problem: Leetcode 2395 - Find subarrays with equal sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-subarrays-with-equal-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: Since our window size is fixed at 2 we just run over the array in O(n) with that window size
# and we add each subarray size into a set for quick look up. Then we check that if the sum of a subarray already
# exists in the array then we can say that two subarrays have same sum and we can return True.

class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums)-2+1):
            sub = nums[i:i+2]
            if sum(sub) in seen:
                return True
            seen.add(sum(sub))
        return False