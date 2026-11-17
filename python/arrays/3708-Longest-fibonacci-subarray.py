
# Problem: Leetcode 3708 - Longest fibonacci subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-fibonacci-subarray/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: While this is a simple two pointer increment problem this question has taught me something very important. 
# the execution of code is not straightforward even when the BigO complexity is same. 
# two nested while loops have manual indexing constrains and multiple paths evven when i gets updated to j and it loos liek O(n).
# but one for loop with a curr varibale is one path forward which is straight. So for JVM JIT compiler this indexing
# with i=j becomes complicated to handle vs one curr variable. Also the CPU path with one variable is more predictable
# also using max specially with python version calls python max function again and again and makes it slow. the if 
# check for max is much faster. 
# now main thing is MEMORY - just one counter variable - the JVM and CPU can keep it inside the memory and the CPU.
# but repeated indexing arithmetic with array out of bounds check is much more complicated for memory.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        #standard two pointers maybe as nothing monotonic in window here
        '''
        mx = 2
        curr = 2
        n = len(nums)
        for i in range(2,n):
            if nums[i] == nums[i-1] + nums[i-2]:
                curr+=1
                if curr>mx:
                    mx = curr
            else:
                curr=2
        return mx
        '''
        #max function and python indexing can be slow
        #if checks are faster
        mx = 2
        i = 0
        while i < len(nums)-1:
            j = i+1
            while j+1 < len(nums) and nums[j+1] == nums[j] + nums[j-1]:
                j+=1
            mx = max(mx, j-i+1)
            i=j
        return mx
        