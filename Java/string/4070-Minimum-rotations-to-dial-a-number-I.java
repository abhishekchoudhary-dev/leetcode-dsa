/* 
Problem: Leetcode 4070 - Minimum rotations to dial a number I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-rotations-to-dial-a-number-I/description/
# Time Complexity: O(n) - as we iterate on words
# Space Complexity: O(1)
# Approach: We simply at each step take the minimum step from current prev number to current either clockwise
# or anticlockwise 10 - val. 
*/

class Solution {
    public int minRotations(String s) {
        int rot = 0;
        int prev = 0;
        for (int i=0;i<s.length();i++){
            //int digit = Integer.parseInt(String.valueOf(s.charAt(i)));
            int digit = s.charAt(i) - '0';
            int val = Math.abs(digit-prev);
            rot += Math.min(val,10-val);
            prev = digit;
        }
        return rot;
    }
}