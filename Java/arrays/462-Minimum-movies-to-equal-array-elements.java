import java.util.Arrays;
/* 
# Problem: Leetcode 462 - Minimum moves to equal array elements II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space used
# Approach: We can brute force by trying every value but that would probably TLE so the idea is to realize for which there is always mathematical proof
# that the minimum distance will be from the median to each value.  to find he median we have to sort the array
# and then we take the median value.
*/

class Solution {
    public int minMoves2(int[] nums) {
        int moves = 0;
        Arrays.sort(nums); //no need to sort can afford this move
        for(int num:nums){
            moves+=Math.abs(nums[nums.length/2]-num);
        }
        return moves;
    }
}