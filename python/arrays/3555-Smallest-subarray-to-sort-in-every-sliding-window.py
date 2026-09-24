# Problem: Leetcode 3555 - Smallest subarray to sort in every sliding window
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We just take every subarray and dont need advanced ideas of swaps and cycle. 
# we just take two pointers and move them inwards from both size till the point till we find sorted element in right place between the sorted array
# and the usual array. The point where the sorting break we know that this segment needs to be sorted. We take that segments length
# and we return its length

from typing import List

class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        def min_swaps(arr):
            s = sorted(arr)
            if arr==s:
                return 0
            left = 0
            right = len(arr)-1
            while left<=right and arr[left] == s[left]:
                left+=1
            while right>=left and arr[right] == s[right]:
                right-=1
            return right-left+1 if right>=left else 0
            
        
        '''
        def min_swap_length(arr):
            if arr == sorted(arr):
                return 0
            arr_pos = sorted(range(len(arr)), key = lambda i:arr[i])
            print("arr_pos",arr_pos)
            i = 0
            window = 0
            while i < len(arr):
                if arr_pos[i]!=i:
                    while i <len(arr) and arr_pos[i]!=i:
                        window+=1
                        i+=1
                    break
                i+=1
            return window
        '''
        ans = []
        for i in range(len(nums)-k+1):
            sub = nums[i:i+k]
            res = min_swaps(sub)
            ans.append(res)

        return ans