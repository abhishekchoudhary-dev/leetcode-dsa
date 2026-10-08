/* 
# Problem: Leetcode 581 - Shortest unsorted continuous subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
# Time Complexity: O(n log n) as we are sorting
# Space Complexity: O(n) as we clone the array
# Approach: We simply compare array with its sorted version and find the start and end points till which we need to sort to 
# make the array sorted. the subarray between start and end will automatically come out to be the shortest
*/

import java.util.*;
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int[] s = nums.clone();
        Arrays.sort(s); //in place so we clone and sort
        if (Arrays.equals(nums,s) || nums.length==1){
            return 0;
        }
        int shortest = Integer.MIN_VALUE;
        Integer start = null;
        int end = 0;
        for (int i=0;i<nums.length;i++){
            if (nums[i]!=s[i]){
                if (start==null){
                    start = i;
                }
                end = Math.max(end,i);
            }
            if(start!=null){
            shortest = Math.max(shortest, end-start+1);}
        }
        return shortest;
    }
}