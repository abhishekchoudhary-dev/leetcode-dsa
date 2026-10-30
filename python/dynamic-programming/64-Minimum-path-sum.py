
#Problem: Leetcode 64-  Minimum path sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-path-sum/description/
# Time Complexity: O(n) as we will the dp array once
# Space Complexity: O(m*n) as we keep our DP array
# Approach: We iterate through the DP array and we fill the first row and column as base case and then
# we basically go to each cells from the previous cell and the path this has least previous sum on the cell above 
# or on the cell on the left. then the last cell of dp array holds the least sum which is our answer



class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        print(dp)
        dp[0][0] = grid[0][0]
        #fill bases cases
        for i in range(1,len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1,len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        #base cases done
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = grid[i][j] + (dp[i-1][j] if dp[i-1][j] < dp[i][j-1] else dp[i][j-1])
        
        return dp[-1][-1]