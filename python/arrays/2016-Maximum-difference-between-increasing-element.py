# Problem: Leetcode 2016 - Maximum differnce between increasing elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We can do an O(n^2) solution as in our naive solution where we check each pair
# Approach2: We can also do it in O(n) more like dynamic programming where we keep the min element seen till now
# and at each step we just check that if current element is greater than the mn seen till now we take their difference in the max variable
# and the then updated the mn seen in every step anyway. This is an O(n) solution

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        mn_seen = nums[0]
        mx_diff = -1
        for i in range(1,len(nums)):
            if nums[i] > mn_seen:
                mx_diff = max(mx_diff,nums[i]-mn_seen)
            mn_seen = min(mn_seen,nums[i])

        return mx_diff

        '''
        mx = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    mx = max(mx, nums[j]-nums[i])
        return mx
        '''