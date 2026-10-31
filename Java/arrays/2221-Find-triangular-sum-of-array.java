import java.util.*;
/* 
# Problem: Leetcode 2221 - Find triangular sum of array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-triangular-sum-of-array/description/
# Time Complexity: O(n) for n elements in nums
# Space Complexity: O(1) as no extra data structure is used
# Approach: We simply follow what the questions asks where we keep assigng the values to newNums as per given formula and 
# keep reassigning newNums to nums
*/

class Solution {
    public int triangularSum(int[] nums) {
            while(nums.length!=1){
                int[] newNums = new int[nums.length-1];
                Arrays.fill(newNums,0);
                for (int i=0;i<nums.length-1;i++){
                    newNums[i] = (nums[i] + nums[i+1])%10;
                }
                nums = newNums;
        
            }
            return nums[0];
    }
}
