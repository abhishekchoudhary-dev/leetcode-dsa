/* 
# Problem: Leetcode 4001 - Find all numbers disappear in an array III
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-III/description/
# Time Complexity: O(n) as we loop over nums once
# Space Complexity: O(n) as we use the answer array
# Approach: We simply loop over nums over each number. Each number is breakpoint so on each of them
# we check if number-1 is greater than or equal the start of current window and also the num is smaller than upper
# if yes we append a sublist of [lower,num-1] and we reset lower to num+1 as next window can only start at num+1
# then we keep moving like this. after the loop its possible that the upper is much bigger than last element
# so we do one check that if after loop the lower <= upper then we append another sublist with
# [lower,upper] and we return our answer
*/

import java.util.*;

class Solution {
    public int[][] findDisappearedNumbers(int[] nums, int lower, int upper) {
        //solution with primitive array inside it
        Arrays.sort(nums);
        List<int[]> ans = new ArrayList<>();
        for(int num : nums){
            if (num < lower) continue;
            if (lower > upper) break;
            if (num-1 >= lower){
                ans.add(new int[]{lower,Math.min(num-1,upper)});
            }
            lower = Math.max(lower,num+1); //must update as old lower used
        }
        if (lower<=upper){
            ans.add(new int[]{lower,upper});
        }
        return ans.toArray(new int[0][]);
        
        /*
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        int write = 0;
        for(int num:nums){
            if (num < lower) continue;
            int currEnd = Math.min(upper,num-1);
            if (currEnd >= lower){
                ans.add(List.of(lower,currEnd));
            }
            lower = Math.max(lower,num+1);

        }
        if (nums[nums.length-1] < upper){
            ans.add(List.of(lower,upper));
        }
        return ans.stream()
        .map(subList -> subList.stream().mapToInt(Integer::intValue).toArray())
        .toArray(int[][]::new);

        //int[] res =  ans.toArray(new int[0][]);
        */
        
    }
}