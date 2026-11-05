#Problem: Leetcode 2008-  Maximum earnings from taxi
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-earnings-from-taxi/description/
# Time Complexity: O(n+ number of rides) as start pointer does not move backwards
# Space Complexity: O(n) as we will have dp array
# Approach: We make a dp array with n+1 slots. for each position on the line we takes its maximum from previous to ensure that this is the maximum we can achieve
# at his posituion. if current already has maximum meaning dp[i] > dp[i-1] then ofcourse it will not update
# then for all future positions which have start from the current i we mark the dp[end] of how much profit we could have at dp[end]
# and then last index of dp will have the answer


class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        rides.sort(key = lambda x:x[0])
        #no monotonic property to do binary search over solution space
        # so we do dp or weighted invterval scheduling
        dp = [0]*(n+1)
        start = 0
        for i in range(n+1):
            if i>0:
                dp[i] = max(dp[i],dp[i-1]) #carrying ? skip position
            while start < len(rides) and rides[start][0] == i:
                s,e,tip = rides[start]
                dp[e] = max(dp[e], dp[i] + (e-s+tip))
                start+=1
        return dp[n]