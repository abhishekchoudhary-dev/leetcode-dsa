/* 
# Problem: Leetcode 3101 - Count alternating subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-alternating-subarrays/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We simply find subarrays that are alternating and we know that the number of subarrays of a subarray of length n lets says
# is n*(n+1)/2 and this way we add to our count. if j is greater than i then we make i = j+1 else we make j++
*/

class Solution {
    public long countAlternatingSubarrays(int[] nums) {
        long cnt = 0;
        int i = 0;
        while (i<nums.length){
            int j = i;
            while (j+1 < nums.length && nums[j] != nums[j+1]){
                j+=1;
            }
            long l = j-i+1;
            cnt += (l*(l+1))/2;
            if (j>i) i = j+1;
            else i++;

        }
        return cnt;
    }
}