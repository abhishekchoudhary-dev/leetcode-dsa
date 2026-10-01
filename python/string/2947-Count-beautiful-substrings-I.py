# Problem: Leetcode 2947 - Count beautiful substrings I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-beautiful-substrings-I/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make and iterate over list of strings
# Approach: We make a prefix array to give number of vowels in a substring in O(1) which will enable use to calculate the consonants fast.
# then based on input size we run an O(n^2) loop in which we check vowels in O(1) so basically 
# we are able to do O(n^2) because of input size of 1000. Once we have vowels and consonants both for a substring
# we are able to check both conditions and if satisfied we increment out count variable.

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        prefix = [0]*(len(s)+1)
        v = c = 0
        cnt = 0
        for i,char in enumerate(s):
            if char in "aeiou":
                v+=1
            prefix[i+1] = v
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if (j-i+1)%2==1:
                    continue
                sub = s[i:j+1]
                v =  prefix[j+1] - prefix[i]
                c = (j-i+1) - v
                if v==c and (v*c)%k==0:
                    cnt+=1
        return cnt