# Problem: Leetcode 647 - Palindromic substrings
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindromic-substrings/description/
# Time Complexity: O(n) - convert each character to lowercase
# Space Complexity: O(1)
# Approach: We use simple brute forcing to check each substring but then we can also use 
# the MANACHER algorith to acheive O(n) time complexity


class Solution:
    def countSubstrings(self, s: str) -> int:
        #brute forcing works here
        cnt = len(s)
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cnt+=1
        return cnt