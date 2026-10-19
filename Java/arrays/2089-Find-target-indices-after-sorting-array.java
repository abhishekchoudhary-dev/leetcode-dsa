/* 
# Problem: Leetcode 2089 - Find target indices after sorting array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
# Approach: Straightforward question to sort and collect indices where element is target
*/

import java.util.*;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int[] copy = nums.clone();
        Arrays.sort(copy);
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<copy.length;i++){
            if (copy[i] == target){
                ans.add(i);
            }
        }
        return ans;
    }
}
