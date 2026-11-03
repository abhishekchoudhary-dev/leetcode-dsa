
/* 
# Problem: Leetcode 3120 - Count the number of special characters in a string
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-in-a-string/description/
# Time Complexity: O(n) - as we go through all the elements of the string in worst case
# Space Complexity: O(k) as we use a HashSet to store unique characters, where k is the number of unique characters
# Approach: We iterate through the string and add each character to a HashSet. Then we iterate through the set and check if a lowercase character has its uppercase counterpart in the set. 
# If so, we increment the count.
*/

package Java.hashmap;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int numberOfSpecialChars(String word) {
        Set<Character> wordSet = new HashSet<>();
        for (char c:word.toCharArray()){wordSet.add(c);}
        int cnt = 0;
        for (char s:wordSet){
            if (Character.isLowerCase(s) && 
            wordSet.contains(Character.toUpperCase(s))) {
                cnt++;
                }

        }
        return cnt;
    }
}