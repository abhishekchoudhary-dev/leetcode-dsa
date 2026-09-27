# Problem: Leetcode 1624 - Largest substring between two equal characters
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We simply keep a hashmap where we add the earliest occurrence of each character and then for the current character
# we check if its already in the hashmap and if it is we take into best the length of the substrings between them and this way we will find the longest substring.


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        best = -1
        d = {}
        for i,char in enumerate(s):
            if char in d:
                best = max(best,i-d[char]-1)
            else:
                d[char] = i
        return best