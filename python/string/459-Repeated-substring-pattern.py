# Problem: Leetcode 459 - Repeated substring pattern
# Difficulty: Easy
# Link: https://leetcode.com/problems/repeated-substring-pattern/description/
# Time Complexity: O(n) - where n is the length of the input address
# Space Complexity: O(n) as we slice the array
# Approach: we run the loop till n//2 as maximum substring can only be till half the length of the string.
# then we slice the current substring and check that if total length//sub string length times the current substring will
# produce the original substring. If it will then we return True else we return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)==1:
            return False
        n = len(s)
        for i in range(len(s)//2):
            sub = s[:i+1]
            if sub * (n//len(sub)) == s:
                return True
        return False 