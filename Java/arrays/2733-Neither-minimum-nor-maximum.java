import java.util.Arrays;
/* 
# Problem: Leetcode 2733 - Neither Minimum nor maximum
# Difficulty: Easy
# Link: https://leetcode.com/problems/neither-minimum-nor-maximum/description/
# Time Complexity: O(n log n) as we sort the array
# Space Complexity: O(1) as no extra data structure is used
# Approach: We simply sort the array so we have min and max and then loop the array and as soon as we find an element
# which is smaller than both we just return it
*/

class Solution {
    public int findNonMinOrMax(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for(int i=1;i<n-1;i++){
            if(nums[i] > nums[0] && nums[i] < nums[n-1]) return nums[i];
        }
        return -1;
    }
}