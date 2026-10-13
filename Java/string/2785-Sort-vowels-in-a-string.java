package java.string;
import java.util.*;
/* 
# Problem: Leetcode 2785 - Sort vowels in a string
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-if-array-is-good/description/
# Time Complexity: O(nlogn ) - for approach 1 and O(n) for counting sort approach 2
# Space Complexity: O(n) for approach1 as we use extra lists and O(n) for counting sort also as we have freq array
# Approach1: First approach uses simple idea where we extra the indices and the vowels and sort them and place them back at those indices directly
# Approach2: Second appraoch says that we take all the vowels of the string and we basically count their occurrence in a frequery array
# then we take a list of sorted vowels and iterate over s and if we find a consonant straight take it into the array
# and if we find a vowel we iterate with a points over sorted vowel list while checking their freq in the freq array we made
# if we find a vowel with remaining freq we append it to ans and return it. Since we are chcking freq in sorted arrays it automatically ensures that 
# we only get the sorted order. */

class Solution {
    boolean isVowel(Character c) {
            return c=='A' || c=='E' || c=='I' || c=='O' || c=='U' || c=='a' ||
            c == 'e' || c=='i' || c=='o' || c=='u';
        }
    public String sortVowels(String s) {
        ArrayList<Character> temp = new ArrayList<>();
        for (char c : s.toCharArray()){
            if(isVowel(c)) temp.add(c);
        }
        Collections.sort(temp);
        //now we write them in
        StringBuilder ans = new StringBuilder();
        int j = 0;
        for (int i=0;i<s.length();i++){
            if(isVowel(s.charAt(i))){
                ans.append(temp.get(j));
                j++;
            }
            else ans.append(s.charAt(i));
        }
        return ans.toString();
}
}
