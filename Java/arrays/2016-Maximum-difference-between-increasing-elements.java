/* 
# Problem: Leetcode 2016 - Maximum differnce between increasing elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We can do an O(n^2) solution as in our naive solution where we check each pair
# Approach2: We can also do it in O(n) more like dynamic programming where we keep the min element seen till now
# and at each step we just check that if current element is greater than the mn seen till now we take their difference in the max variable
# and the then updated the mn seen in every step anyway. This is an O(n) solution
*/

class Solution {
    public int maximumDifference(int[] nums) {
        int mxDiff = -1;
        int mnSeen = nums[0];
        for(int i=1;i<nums.length;i++){
            if (nums[i]>mnSeen){
                mxDiff = Math.max(mxDiff,nums[i]-mnSeen);
            }
            mnSeen = Math.min(mnSeen,nums[i]);
        }
        return mxDiff;
    }
}
