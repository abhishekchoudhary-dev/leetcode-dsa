/* 
# Problem: Leetcode 325 - Maximum size subarray sum equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use as hashmap
# Approach: A very standard implementation of a hashmap based prefix sum with a sentinal value to start with
# addding sum 0 and index -1
*/

import java.util.*;


class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int mx = 0;
        int currSum = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        map.put(0,-1);
        for (int right=0;right<nums.length;right++){
            currSum += nums[right];
            if (map.containsKey(currSum - k)) mx = Math.max(mx, right - map.get(currSum - k));
            if (!map.containsKey(currSum)) map.put(currSum, right);
        }
        return mx;
    }
}