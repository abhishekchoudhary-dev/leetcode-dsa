# Problem: Leetcode 1763 - Longest nice substring
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-nice-substring/description/
# Time Complexity: O(n) - as we iterate through the string
# Space Complexity: O(1) 
# Approach: We basically brute force it since input size is small. we cut the substrings and check if it has both upper and lower of all the alphabets in it. 
# if yes we compare its length to answer and if its bigger we reassign it. For small efficiency gain we can
# put the char into a set to not recheck it if is lower or upper version is already seen.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        if len(s)==1:
            return ""
        def check(s):
            seen =set()
            for char in s:
                if char in seen: continue
                if char.islower():
                    if char.upper() not in s:
                        return False
                else:
                    if char.lower() not in s:
                        return False
                seen.add(char)
            return True
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                sub = s[i:j+1]
                if check(sub):
                    if len(sub) > len(ans):
                        ans = sub
        return ans
