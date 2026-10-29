/* 
# Problem: Leetcode 4089 - Count subarrays with loose bounds
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-subarrays-with-loose-bounds/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We cannot look at all the subrrays as the input size of 10^5 does not allow that
# so we just see all the values that can occur in the subarray and then we find the longest run beefore we hit a value
# which is less than minK and more than maxK. then this value will now allow this particular subarray to be included
# so at this point we just add all the possible subarrays we can take from the previous run 
# and reset the run size to zero. the subarrays from previous run woud be n*n+1//2
*/ 

class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long res = 0;
        long run = 0;
        for(int i = 0 ; i <nums.length; i++){
            if (nums[i]>=minK && nums[i]<=maxK){
                run++;
            }
            else{
                res += run*(run+1)/2;
                run = 0;
            }
        }
        if (run!=0) res+=run*(run+1)/2;
        return res;
    }
}