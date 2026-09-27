# Problem: Leetcode 3719 - Longest balanced subarray I
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-balanced-subarray-I/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we keep sets
# Approach: Due to small input constraints we just move over each possible subarray keeping elements in a set and then at the end of the loop
# checking if the subarray has equal number of even and odds and for each j we keep updating our best to find the best subarray

from typing import List
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        best = 0
        for i in range(len(nums)):
            e = set()
            o = set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    e.add(nums[j])
                else:
                    o.add(nums[j])
                if len(e) == len(o):
                    best = max(best,j-i+1)
        return best
        '''
        prefirx+hashmap fails
        d = {}
        d[0]=-1
        e = set()
        o = set()
        best = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                e.add(nums[i])
            else:
                o.add(nums[i])
            #diff = even - odd
            diff = len(e) - len(o)
            if diff in d:
                best = max(best,i - d[diff])
            else:
                d[diff] = i
        return best
        '''