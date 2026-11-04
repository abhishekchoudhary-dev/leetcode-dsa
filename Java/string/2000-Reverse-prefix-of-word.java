package Java.string;
/* 
Problem: Leetcode 2000 - Reverse prefix of word
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-prefix-of-word/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We find the first occurrence of the target character and slice the string and reverse it 
# and the remaining string is appended to it.
*/
class Solution {
    private String rev(String org){
        StringBuilder reversed = new StringBuilder();
        for (int i = org.length()-1;i>=0;i--){
            reversed.append(org.charAt(i));
        }
        return reversed.toString();
    }
    public String reversePrefix(String word, char ch) {
        for(int i=0;i<word.length();i++){
            if (word.charAt(i)==ch){
                word = rev(word.substring(0,i+1)) + word.substring(i+1,word.length());
                break;
            }
        }
        return word;
    }
} {
    
}
