/* 
Problem: Leetcode 2027 - Minimum moves to convert string
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-moves-to-convert-string/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We need to optimize by not unnecessarily checking every group of 3 elements but rather only changin them when 
# the current element is X as at that moment we have to change it to O and then we jump our index 3 places
# as the next 3 element have already be changed top 'O' and we dont want to waste a move.
*/

class Solution {
    public int minimumMoves(String s) {
        if(!s.contains("X")) return 0;
        int i = 0;
        int ops = 0;
        while (i < s.length()){
            if (s.charAt(i) == 'X'){
                ops++;
                i+=3;
                continue;
            }
            i++;
        }
        return ops;
    }
}
