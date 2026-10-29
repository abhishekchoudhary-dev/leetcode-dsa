/* 
Problem: Leetcode 4092 - binary digit score
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-digit-score/description/
# Time Complexity: O(k) with k being the number of bits in the number
# Space Complexity: O(1) as no extra space is used
# Approach - We just find the set bits in both numbers and return the values as per the formulas provided 
# in the question
*/

class Solution {
    private int findSetBits(int num){
        int cnt = 0;
        while (num!=0){
            if ((num&1)!=0) cnt++;
            num>>=1;
        }
        return cnt;
    }
    public int calculateScore(int a, int b) {
        int s1=0;int s2=0;
        int score = 0;
        s1 = findSetBits(a);
        s2 = findSetBits(b);
        if (s1>=s2){
            score = s1*s2;
        }
        else score = s2/s1;
        return score;
    }
}
