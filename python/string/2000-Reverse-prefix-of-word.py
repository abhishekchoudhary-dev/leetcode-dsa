
#Problem: Leetcode 2000 - Reverse prefix of word
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-prefix-of-word/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We find the first occurrence of the target character and slice the string and reverse it 
# and the remaining string is appended to it.


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i,c in enumerate(word):
            if c == ch:
                word = word[0:i+1][::-1] + word[i+1:]
                break
        return word