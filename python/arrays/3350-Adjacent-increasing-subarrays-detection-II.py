# Problem: Leetcode 3350 - Adjacent increasing subarrays detection II
# Difficulty: Medium
# Link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-II/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use forward array to store things
# Approach: After binary search on solution space, we keep a forward len array which is a RUN LENGTH array like we have runs
# and this array can tell us the longest length of strictly increasing sequence starting at forward[i].
# so if both forward[i] >= k and forward[i+k]>=k meaning both have runs starting from them which are at least k length
# we return true from the feasible function and continue our search then.

from typing import List
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        '''TLE
        def is_strictly_increasing(arr):
            return all(arr[i]<arr[i+1] for i in range(len(arr)-1))
        def isfeasible(arr,k):
            for i in range(len(nums)-2*k+1):
                first = nums[i:i+k]
                second = nums[i+k:i+2*k]
                if is_strictly_increasing(first) and is_strictly_increasing(second):
                    return True
            return False
        '''
        n = len(nums)
        forward = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                forward[i] = forward[i + 1] + 1

        def isfeasible(k):
            for i in range(n - 2 * k + 1):
                if forward[i] >= k and forward[i + k] >= k:
                    return True
            return False

        left = 0
        right = (len(nums)//2) + 1
        ans = 0
        #binary search on search space
        while left < right:
            mid = (left+right)//2
            if isfeasible(mid):
                ans = mid
                left = mid+1
            else:
                right = mid
        return ans
