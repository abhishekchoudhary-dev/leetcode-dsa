# Problem: Leetcode 3095 - Shortest subarray with OR at least K I
# Difficulty: Easy
# Link: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Based on input size we just brute force and take all the possible subarrrays and check if they have OR
# greater than or equal to k and then we can just take it in the best value and return best
# at the end

from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        #brute force solution
        def calculate(arr):
            bitwiseOR = arr[0]
            for e in arr:
                bitwiseOR|=e
            return bitwiseOR>=k
        best = float('inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub = nums[i:j+1]
                if calculate(sub):
                    best = min(best,j-i+1)
        return best if best!=float('inf') else -1
        '''
        
        smallest = float('inf')
        bitwiseOR = nums[0]
        length  = 0
        for right in range(len(nums)):
            bitwiseOR|=nums[right]
            if bitwiseOR >= k:
                length+=1
            else:
                length = 1 #start bew subarray from current
                bitwiseOR = nums[right]
            smallest = min(smallest,length)
            
        return smallest if smallest!=float('inf') else -1
        '''