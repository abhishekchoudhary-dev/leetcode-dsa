/*
# Problem: Leetcode 42 - Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a stack to push and pop elements
# Approach: # Approach: We start with valid stack starting at -1 to deal with first element being closing bracket which is then pooped
# and 0 index is added. basically the index added is of the invalid parentheses list where the last invalid streak end
# so that we can subtract it from valid one and get the length of the valid string
# when we find open brakcet we keep appending the index and when we find closing bracket we pop the last index and check if stack is empty
# if yes we append current index as that means everything upto current index that was valid was already seen.
*/

package Java.stackanddeque;
import java.util.*;

class Solution {
    public int longestValidParentheses(String s) {
        if (s.length()==0) return 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.addLast(-1);
        int best = 0;
        for (int i=0;i<s.length();i++){
            if (s.charAt(i)=='(') stack.addLast(i);
            else{
                stack.removeLast();
                if (stack.isEmpty()) stack.addLast(i);
                else{
                    best = Math.max(best,i-stack.peekLast());
                }
            }
        }
        return best;
        
    }
}