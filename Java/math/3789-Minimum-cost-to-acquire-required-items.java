/* 
Problem: Leetcode 3789- Minimum cost to acquire required items
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach - We use greedy logic that if costBoth is greater or equal then its always beneficial to just buy them individually and cost would be minimum.
# but if costBoth is lower than cost1+cost2 then its beneficial to buy costBoth upto min(need1,need2)
# and buy the rest of the items of whichever out of type1 and type2 is lefton their own cost.
# however i am taking other case also that we buy all with costBoth as we are not checking how cost both compares to cost1 and cost2 individually
# hence we just compare and return min of both
*/

class Solution {
    public long minimumCost(long cost1, long cost2, long costBoth, long need1, long need2) {
        //input variables have to be explicity casted to long
        //so we just change the input function parameter to long itself.
        if (costBoth < cost1+cost2){
            long first = Math.max(need1,need2) * costBoth;
            long second = Math.min(need1,need2) * costBoth + (need1 - Math.min(need1,need2))*cost1 + (need2 - Math.min(need1,need2)) * cost2;
            return (long)Math.min(first,second);

        }
        else{
            return (long)need1*cost1+need2*cost2;
        }
    }
}