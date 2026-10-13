/* 
# Problem: Leetcode 2780 - Minimum index of a valid split
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We make a freq hashmap and find the most frequent element and its frequency. then we start iterating the array
# and the very first momement when value of dominant element crosses half of the array seen we checkign if its dominant in the second half also
# Because this is the best possible smallest index which has highest possibility of finding dominant index in second part
*/

import java.util.*;

class Solution {
    public int minimumIndex(List<Integer> nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int num: nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        //System.out.println(map);
        int mx = 0;
        int key = 0;
        for(Map.Entry<Integer,Integer> entry: map.entrySet()){
            if (entry.getValue() > mx){
                mx = entry.getValue();
                key = entry.getKey();
            }
        }
        int cnt = 0;
        int rem_dominant = mx;
        for(int i = 0;i<nums.size();i++){
            if (nums.get(i) == key) {
                cnt++;
                if (cnt > (i+1)/2){
                    int rem = nums.size() - i - 1;
                    rem_dominant = mx - cnt;
                    if(rem_dominant>rem/2){
                        return i;
                    }
                }
            }

        }
        return -1;
    }
}