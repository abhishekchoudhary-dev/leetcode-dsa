package Java.stackanddeque;
/* 
# Problem: Leetcode 856 - Score of parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/score-of-parantheses/description/
# Time Complexity: O(n)
# Space Complexity: O(1) for balance approach and O(n) for stack
# Approach1: We just maintain the depth that we are in and if we find complete valid bracket with 0 depth
# we add 2 to the power 0 to result which is one and correct, and if there is depth it will account for in the formula 2**depth.
# So everytime we find closing bracket we check if the bracket just before is opening and if yes then we add to score based on current depth we are at
# if its not opening means we are just coming out of the depth without adding to score. {
*/

class Solution {
    public int scoreOfParentheses(String s) {
        int depth = 0;
        int score = 0;
        for(int i=0;i<s.length();i++){
            if (s.charAt(i)=='('){
                depth+=1;
            }
            else{
                depth-=1;
                if(s.charAt(i-1)=='(') {
                    score+=Math.pow(2,depth);
                }
            }
        }
        return score;
    }
}