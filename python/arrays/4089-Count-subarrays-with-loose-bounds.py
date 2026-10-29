# Problem: Leetcode 4089 - Count subarrays with loose bounds
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-subarrays-with-loose-bounds/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We cannot look at all the subrrays as the input size of 10^5 does not allow that
# so we just see all the values that can occur in the subarray and then we find the longest run beefore we hit a value
# which is less than minK and more than maxK. then this value will now allow this particular subarray to be included
# so at this point we just add all the possible subarrays we can take from the previous run 
# and reset the run size to zero. the subarrays from previous run woud be n*n+1//2

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        run = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] <= maxK and nums[i]>=minK:
                run+=1
            else:
                res+=(run*(run+1))//2
                run=0
        #caatch remaining run
        if run:
            res+=run*(run+1)//2
        return res
        