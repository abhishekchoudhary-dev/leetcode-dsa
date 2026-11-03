/* 
# Problem: Leetcode 4097 - Minimum value of merged integers
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-value-of-merged-integers/description/
# Time Complexity: O(k) with k being digits as we concatenate each pair with total k digits
# Space Complexity: O(1) as we do not use extra space
# Approach: Straighfotward question we keep jumping index with 2 and concatenating two integerss and comparing the value with 
# the running maximum
*/

class Solution {
    public int minMergedInteger(int[] nums) {
        int mx = Integer.MAX_VALUE;
        for(int i=0;i<nums.length;i+=2){
            String value = String.valueOf(nums[i]) + String.valueOf(nums[i+1]);
            Integer v = Integer.valueOf(value);
            mx = Math.min(mx,v);

        }
        return mx;
    }
}