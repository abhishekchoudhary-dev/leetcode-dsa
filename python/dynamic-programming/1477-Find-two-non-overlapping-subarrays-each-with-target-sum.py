# Problem: Leetcode 1477 - Find two non overlapping subarrays each with target sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-two-non-overlapping-subarrays-each-with-target-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only keep last state
# Approach: We use dynamic programming as we cannot let go of any sub array as sliding window approach below fails.
# as we dropping the subarrays that might have a smaller replacement by keeping a wall.So we use prefix sum + hashmap
# but we employ dynamic programming where dp[j+1] is the best subarray seen till dp[j] and then when target is found from (j,i]  then
# we can calculate the subarray length by taking from dp[j+1] + length which will capture the best subarray equal to target seen till index j
# and this way we do not lose a subarray.

from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        d = {0:-1}
        curr_sum = 0
        dp = [float('inf')] * (len(arr)+1)
        ans = float('inf')
        for right in range(len(arr)):
            curr_sum += arr[right]
            dp[right+1] = dp[right]
            if curr_sum - target in d:
                j = d[curr_sum-target]
                length = right - j
                if dp[j+1] < float('inf'):
                    ans = min(ans,dp[j+1]+length)
                dp[right+1] = min(dp[right+1],length)
            d[curr_sum] = right
        return ans if ans < float('inf') else -1
        '''
        #simple sliding window
        # fails
        left = -1
        lens = []
        d = {}
        d[0]= -1
        curr_sum = 0
        for right in range(len(arr)):
            curr_sum+=arr[right]
            if curr_sum - target in d:
                if d[curr_sum-target] >= left:
                    lens.append(right - d[curr_sum-target])
                    left = right
                    d[curr_sum] = right
            else:
                d[curr_sum] = right
        print(d)
        print(lens)
        if len(lens)<2:
            return -1
        lens.sort()
        return lens[0]+lens[1]
        '''