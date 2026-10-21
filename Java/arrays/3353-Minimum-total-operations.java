package Java.arrays;

/* 
# Problem: Leetcode 3353 - Minimum total operations
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-total-operations/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We simply need observation that the element that are same move together and those who are diff move separately so 
# a separate element will take an individual move to be made equal. Since we are dealing with prefix
# we take a sentinal value and we keep moving backwards with it taking count of the number of different eleement.
# the sentinal is ofcourse the last element as all element in prefix have to be made equal. then we return cnt
*/

class Solution {
    public int minOperations(int[] nums) {
        int cnt = 0;
        for (int i=nums.length-2;i>=0;i--){
            if(nums[i]!=nums[i+1]) cnt++;
        }
        return cnt;
    }
}
