# Problem: Leetcode 4093 - Maximum sum after at most K rearragement
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-sum-after-at-most-k-rearragements/description/
# Time Complexity: O(n) as sorting of inidividual numbers is O(k) with k being max size of 9
# Space Complexity: O(n) as we make gain per index array
# Approach: We do not know how much the maximum gain can be by choosing. So we calculate the gain for every index
# by looping once and then keeping the gain per index into an array. Once we have that then since k operations are allowed
# we sort this array to have the maximum gains first by reverse sort and pick up the top k values
# then we return the sum of nums and the sum of top k values of gain array as that is the maximum gain we can have


class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        #just calculate gains directly
        gain_per_index = [0]*len(nums)
        for i in range(len(nums)):
            s = int(''.join(sorted(str(nums[i]),reverse=True)))
            if s > nums[i]:
                gain_per_index[i] = s-nums[i]
        gain_per_index.sort(reverse=True)
        return sum(nums) + sum(gain_per_index[0:k])