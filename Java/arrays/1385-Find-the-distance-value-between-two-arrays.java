/* 
# Problem: Leetcode 1385 - Find distance value between two arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-distance-value-between-two-arrays/description/
# Time Complexity: O(n)
# Space Complexity: O(n) 
# Approach: We just run a nested loop based on constraints and check if an element has distance less than 
# d for values in arr2 and increment count
*/

class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int cnt = 0;
        for(int num1: arr1){
            boolean possible = true;
            for(int num2:arr2){
                if (Math.abs(num1-num2)<=d){
                    possible = false;
                    break;
                }
            }
            if(possible) cnt++;
        }
        return cnt;
    }
}