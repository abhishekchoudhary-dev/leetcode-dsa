/* 
# Problem: Leetcode 560 - Subarray sum equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We simply keeping adding the count of the subarray sums seen to the hashmap and then we take 
# the amount of subarrays seen for curr_sum - k meaning these subarrays have sum k and add that to the result. We use
# get or default here so that is key doesnt exist we add 0 to the hashmap and then the new entry is made into the hashmap
*/

import java.util.HashMap;

class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0,1); //0 sum already seen 1 time
        int res = 0;
        int curr_sum = 0;
        for (int right=0;right<nums.length;right++){
            curr_sum+=nums[right];
            res+= map.getOrDefault(curr_sum-k,0);
            if (map.containsKey(curr_sum)) {map.put(curr_sum,map.get(curr_sum)+1);}
            else {
                map.put(curr_sum,1);
            }
            
        }
        return res;
    }
}