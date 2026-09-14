/* 
# Problem: Leetcode 961 - N repeated element in size 2N arrat
# Difficulty: Easy
# Link: https://leetcode.com/problems/n-repeated-element-in-size-2N-array/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: We just check for the first repeated value and we immediately return. we can have a final return 0 or throw a runtTime exception if 
# if the code flow reaches there as it was not supposed to.
*/
class Solution {
    public int repeatedNTimes(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num:nums){
            if (s.contains(num)){
                return num;
            }
            s.add(num);
        }
     return 0;
    }
}