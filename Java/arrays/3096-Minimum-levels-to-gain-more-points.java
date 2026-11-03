package Java.arrays;
/* 
# Problem: Leetcode 3096- Minimum levels to gain more points
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we keep prefix sum
# Approach: Simple prefix sum problem where we take the prefix sum and then we loop over it
# and then we see if at any point prefix sum crosses the sum of the remaining possible array
# and we immediately return the index. if loop ends we return -1
*/
import java.util.*;
class Solution {
    public int minimumLevels(int[] possible) {
        int[] prefix = new int[possible.length+1];
        Arrays.fill(prefix,0);
        int score = 0;
        for(int i=0;i<possible.length;i++){
            if (possible[i]==1) score++;
            else score--;
            prefix[i+1] = score;
        }
        for (int i=1;i<prefix.length-1;i++){
            if (prefix[i] > prefix[prefix.length-1] - prefix[i]){
                return i;
            }

        }
        return -1;

    }
}
