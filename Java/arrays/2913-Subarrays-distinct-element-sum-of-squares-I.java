package Java.arrays;
import java.util.*;
/* 
# Problem: Leetcode 2913 - Subarrays distinct element sum of squares I
# Difficulty: Easy
# Link: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-I/description/
# Time Complexity: O(n^2) - as we go through the nested loop
# Space Complexity: O(n) as we make a subarray
# Approach1: Since constraints are small we just check in nested loop each subarray and take the square of 
# the number of unique elements and add that in the total. Since the unique elements in not a monotonic property, 
# hence we are not able to use prefix sums.
*/

class Solution {
    public int sumCounts(List<Integer> nums) {
        int total = 0;
        for (int i =0;i<nums.size();i++){
            for(int j = i;j<nums.size();j++){
                List<Integer> sub = nums.subList(i,j+1);
                Set<Integer> set = new HashSet<>(sub);
                total += Math.pow(set.size(),2);
            }
        }
        return total;
    }
}