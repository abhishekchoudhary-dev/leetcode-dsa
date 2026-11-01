/* 
# Problem: Leetcode 453 - Minimum moves to equal array elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space used
# Approach: Since we are mandated to take n-1 elements every time we have to realize that 
# the smallest element has to close the gap to each bigger element individually and that is what we do
*/

class Solution {
    public int minMoves(int[] nums) {
        int mn = Integer.MAX_VALUE;
        for (int num:nums){
            if (num < mn) mn=num;
        }
        int moves = 0;

        for(int num:nums){
            moves += (num - mn);
        }
        return moves;
    }
}