# Problem: Leetcode 3551 - Minimum swaps to sort by digit sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We use the standard idea where we need to find the arr_pos array wheich will hold the position of the index where the actual element which will finally be placed in the sorted array resides.
# For this we have to first find digit sum array and sort based on digit sum and if there is a tie we sort by nums[i].
# Then we detect cycles in this arr_pos as each cycle needs cycle_size-1 sorts to be sorted.
# this is because each array is just a permutation of its sorted version. and this permutation mapping produces disjoint cycles
# and each cycle needs cycle_size - 1 sorts to sort.

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digit_sums = [0]*len(nums)
        for i,num in enumerate(nums):
            digit_sums[i] = sum(int(d) for d in str(num))

        visited = [False] * len(nums)
        arr_pos = sorted(range(len(nums)),key = lambda i:(digit_sums[i],nums[i]))
        swaps = 0
        for i in range(len(nums)):
            if visited[i] or nums[i]==i:
                continue
            cycle_size = 0
            j=i
            while not visited[j]:
                visited[j]=True
                j = arr_pos[j]
                cycle_size+=1
            swaps+=cycle_size-1
        return swaps