package Java.stackanddeque;
/* 
# Problem: Leetcode 921 - Minimum add to make parantheses valid
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-add-to-make-parantheses-valid/description/
# Time Complexity: O(n)
# Space Complexity: O(n) due to stack(deque) usage
# Approach1: We are just add opening brackets to stack and if we find a closing brackets
# we just check if there is any opening bracket and a pair can be formed and in this case we pop from the stack
# otherwise we add the closing bracket also to the stack as at the end we will have to add a pair to balance it
# so basically all the unbalanced brackets are left in the stack
*/

import java.util.*;

class Solution {
    public int minAddToMakeValid(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        for(Character c: s.toCharArray()){
            if (c.equals('(')) stack.addLast(c);
            else{
                if(!stack.isEmpty() && stack.peekLast().equals('(')) stack.removeLast();
                else {stack.addLast(c);}
            }
        }
        return stack.size();
    }
}