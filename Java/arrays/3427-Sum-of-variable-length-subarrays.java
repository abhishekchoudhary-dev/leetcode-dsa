package Java.arrays;

/* 
# Problem: Leetcode 3411 - Sum of variable length subarrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-varibale-length-subarrays/description/
# Time Complexity: O(n^2)
# Space Complexity: O(n) as we calculate prefix sums
# Approach: We take start as length of subarray is variable and then since java does not have a in built sum method
# and we run a loop to take sum of the subarray. Since subarray length varies some type of prefix sum seems complicated
# Also inpur size is small enough to use a nested loop
*/ 

class Solution {
    public int subarraySum(int[] nums) {
        int total = 0;
        for (int i =0;i <nums.length;i++){
            int start = Math.max(0,i-nums[i]);
            for(int j = start;j<=i;j++) total+=nums[j];
        }
        return total;
        
    }
} 
