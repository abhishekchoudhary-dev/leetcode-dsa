/* 
# Problem: Leetcode 4099 - Minimum operations to sort with locked indices
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-sort-with-locked-indices/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we do not use extra space
# Approach: Since input size is 2000 we can run a usual nested sorting loop like bubble sort 
# and before bubbling we keep chcking the posiitons being swapped so that if they are locked we increase the unlock count by 1
# if unlock count during loop exceeds k then we immediately return -1 else we keep going
# and at the end we return swaps + unlock
*/

class Solution {
    public int minOperations(int[] nums, int[] locked, int k) {
        int swaps = 0;
        int unlocks = 0;
        for (int i=0; i < nums.length-1;i++){
            for(int j=i+1; j<nums.length;j++){
                if (nums[i]>nums[j]){
                    if ((locked[i])==1){
                        unlocks++;
                        locked[i]=0;
                    }
                    if((locked[j])==1){
                        unlocks++;
                        locked[j]=0;
                    }
                    if (unlocks>k) return -1;
                    swaps++;
                }
            }
        }
        return swaps+unlocks;
    }
}
