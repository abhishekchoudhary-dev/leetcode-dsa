import java.util.*;
/* 
# Problem: Leetcode 3644 - Maximum k to sort a permutation
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
# Approach: Main idea is to figure out which elements need to be moved and finding their common set bit. Only is 
# all the elements have a common set bit can their be a k which will be result of their AND.
# as only that bit will figure in the and operation as every other alternating bits go to zero
*/ 
class Solution {
    public int sortPermutation(int[] nums) {
        int[] s = nums.clone();
        Arrays.sort(s);
        Integer k = null;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=s[i]){
                if(k == null) k = nums[i];
                k&=nums[i];
            }
        }
        if(k==null) return 0;
        return k;
    }
}