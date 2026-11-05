import java.util.*;

/* 
Problem: Leetcode 2008-  Maximum earnings from taxi
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-earnings-from-taxi/description/
# Time Complexity: O(n+ number of rides) as start pointer does not move backwards
# Space Complexity: O(n) as we will have dp array
# Approach: We make a dp array with n+1 slots. for each position on the line we takes its maximum from previous to ensure that this is the maximum we can achieve
# at his posituion. if current already has maximum meaning dp[i] > dp[i-1] then ofcourse it will not update
# then for all future positions which have start from the current i we mark the dp[end] of how much profit we could have at dp[end]
# and then last index of dp will have the answer
*/

class Solution {
    public long maxTaxiEarnings(int n, int[][] rides) {
        Arrays.sort(rides, Comparator.comparingInt(a -> a[0]));
        long[] dp = new long[n+1];
        Arrays.fill(dp,0);
        int start = 0;
        for (int i=0;i<n+1;i++){
            if (i>0){
                dp[i] = Math.max(dp[i-1],dp[i]);
            }
            while (start < rides.length && rides[start][0]==i){
                int[] vals = rides[start]; //cant deconstruct like python so 
                //deconstruct into an array like this
                int s =vals[0],e = vals[1], tip = vals[2];
                dp[e] = Math.max(dp[e], dp[i]+(e-s+tip));
                start++;
            }
        }
        return dp[n];
    }
}