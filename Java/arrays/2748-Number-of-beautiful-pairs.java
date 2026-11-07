/* 
# Problem: Leetcode 2748 - Number of beautiful pairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-beautiful-pairs/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We just do a nested loop based on constraints and then we just check the gcd of the two numbers
# that is the first digit of first number and second of another to be 1. if yes then we increment our pair count
*/

class Solution {
    private int gcd(int a, int b){
        if (b==0) return a;
        return gcd(b,a%b);
    }
    public int countBeautifulPairs(int[] nums) {
        int cnt = 0;
        for(int i=0;i<nums.length-1;i++){
            String s = String.valueOf(nums[i]);
            //int fd = Integer.parseInt(s.charAt(0));
            int fd = Character.getNumericValue(s.charAt(0));
            for(int j=i+1; j<nums.length; j++){
                int sd = nums[j]%10;
                if (gcd(fd,sd)==1) {cnt++;}
            }
           
        }
        return cnt;
    }
} {
    
}
