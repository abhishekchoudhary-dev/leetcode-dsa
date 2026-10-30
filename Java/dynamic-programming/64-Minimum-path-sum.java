import java.util.Arrays;

/* 
Problem: Leetcode 64-  Minimum path sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-path-sum/description/
# Time Complexity: O(n) as we will the dp array once
# Space Complexity: O(m*n) as we keep our DP array
# Approach: We iterate through the DP array and we fill the first row and column as base case and then
# we basically go to each cells from the previous cell and the path this has least previous sum on the cell above 
# or on the cell on the left. then the last cell of dp array holds the least sum which is our answer
*/

class Solution {
    public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        for (int[] row: dp){
            Arrays.fill(row,0); //can also fill in nested loops
        }
        //initialize
        dp[0][0] = grid[0][0];
        for (int i = 1; i<grid[0].length;i++){
            dp[0][i] = grid[0][i] + dp[0][i-1];
        }
        for (int i = 1; i < grid.length; i++){
            dp[i][0] = grid[i][0] + dp[i-1][0];
        }
        for(int i = 1;i<grid.length;i++){
            for(int j = 1; j<grid[0].length;j++){
                if(dp[i-1][j] < dp[i][j-1]) dp[i][j] = grid[i][j] + dp[i-1][j];           
                else{
                    dp[i][j] = grid[i][j] + dp[i][j-1];
                }
            }
        }
        return dp[grid.length-1][grid[0].length-1];
    }
} {
    
}
