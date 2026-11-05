# Problem: Leetcode 4001 - Find all numbers disappear in an array III
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-III/description/
# Time Complexity: O(n) as we loop over nums once
# Space Complexity: O(n) as we use the answer array
# Approach: We simply loop over nums over each number. Each number is breakpoint so on each of them
# we check if number-1 is greater than or equal the start of current window and also the num is smaller than upper
# if yes we append a sublist of [lower,num-1] and we reset lower to num+1 as next window can only start at num+1
# then we keep moving like this. after the loop its possible that the upper is much bigger than last element
# so we do one check that if after loop the lower <= upper then we append another sublist with
# [lower,upper] and we return our answer

class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans = []
        nums.sort()
        start = lower
        end = upper
        for num in nums:
            if num < start: continue
            curr_end = num-1
            curr_end = min(curr_end,upper)
            if curr_end>=start:
                ans.append([start,curr_end])
            start = max(start,num+1) #always needs reset
        if start <= upper:
            ans.append([start,upper])
        return ans
