# Problem: Leetcode 3789- Minimum cost to acquire required items
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach - We use greedy logic that if costBoth is greater or equal then its always beneficial to just buy them individually and cost would be minimum.
# but if costBoth is lower than cost1+cost2 then its beneficial to buy costBoth upto min(need1,need2)
# and buy the rest of the items of whichever out of type1 and type2 is lefton their own cost.
# however i am taking other case also that we buy all with costBoth as we are not checking how cost both compares to cost1 and cost2 individually
# hence we just compare and return min of both


class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        minCost = 0
        if costBoth < cost1+cost2:
            first = max(need1,need2) * costBoth
            second = min(need1,need2) * costBoth + (need1 - min(need1,need2)) * cost1 + (need2 - min(need1,need2)) * cost2
            return min(first,second)
        elif costBoth>= cost1+cost2:
            return cost1*need1 + cost2*need2