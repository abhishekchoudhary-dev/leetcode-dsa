/* 
Problem: Leetcode 3099 - Harshad Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/harshad-number/description/
# Time Complexity: O(k) where k is the number of digits of the number
# Space Complexity: O(1)
# Approach - We simply find digit sum and then check if its divides or not
*/

class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int original = x;
        while (x > 0){
            sum += (x%10);
            x/=10;
        }
        if((original%sum)==0) return sum;
        return -1;

    }
}