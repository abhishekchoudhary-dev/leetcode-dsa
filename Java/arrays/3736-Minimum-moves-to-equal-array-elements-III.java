/* 
# Problem: Leetcode 3736 - Maximum moves to equal array elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
# Time Complexity: O(n) - find max and then compare each element with it
# Space Complexity: O(1)
# Approach: Since each element is individual now each one's distance needs to be compared with the maximum element
# and then the total has to be calculated by diff of each element with the maximum value
*/ 

class Solution {
    public int minMoves(int[] nums) {
        int mx = 0;
        for (int num:nums) mx= Math.max(mx,num);
        int total = 0;
        for(int num:nums) total+=(mx-num);
        return total;
    }
}