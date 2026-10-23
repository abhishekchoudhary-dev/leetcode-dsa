/* 
# Problem: Leetcode 2869 - Minimum operations to collect elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimun-operations-to-collect-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(n) for the answer array
# Approach: We simply loops backwards and keep collecting if elements is less than k and we keep collection as a set
# to ignore duplicates. Then if the length of s reaches k it means every element has been collected
# so we break and return the operations
*/

import java.util.*;

class Solution {
    public int minOperations(List<Integer> nums, int k) {
        Set<Integer> set = new HashSet<>();
        int ops = 0;
        for (int i=nums.size()-1;i>=0;i--){
            ops+=1;
            if(nums.get(i) <= k){
            set.add(nums.get(i));
            if (set.size() == k) break;
            }
        }
        return ops;
    }
}