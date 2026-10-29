/* 
# Problem: Leetcode 4088 - Difference between peaks and valleys
# Difficulty: Easy
# Link: https://leetcode.com/problems/difference-between-peaks-and-valleys/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We just keep on diff variable for both sides and everytime we find a hill we add it and then 
# evertime we find a valley we substract it and return diff at the end
*/ 

class Solution {
    public int peakValleyDifference(int[] nums) {
        int diff = 0;
        for (int i=1;i<nums.length-1;i++){
            if (nums[i]>nums[i-1] && nums[i]>nums[i+1]) diff+=nums[i];
            if (nums[i]<nums[i-1] && nums[i]<nums[i+1]) diff-=nums[i];
        }
        return diff;
    }
}