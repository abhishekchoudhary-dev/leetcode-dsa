# Problem: Leetcode 408 - Valid word abbreviation
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-word-abbreviation/description/
# Time Complexity: O(n) as we iterate over both string with two pointers
# Space Complexity: O(1) as no data structure is used
# Approach: We need to understand that abbr is just abbreviation of the work so if we use two pointers and run them parallely on both the strings
# then both should reach the end of the string together.  When we find a char in abbr we compare it with char in word and if they are equal we increment both pointers
# and if not then we just return False. Otherwise if its a digit we check further if its a 2or3 digit number and find the number.
# then we increment i number times so get it in sync with abbr again. Then we keep moving both and if our logic is correct both should reach enter together.
# we check this in our return statement and return True based on that

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j =0
        while i<len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] == abbr[j]:
                    i+=1
                    j+=1
                else:
                    return False
            elif abbr[j].isdigit():
                if abbr[j]=='0':
                    return False
                start = j
                while j+1<len(abbr) and abbr[j+1].isdigit():
                    j+=1
                num = int(abbr[start:j+1])
                j+=1
                if num>len(word):
                    return False
                while num>0:
                    i+=1
                    num-=1
        return i==len(word) and j==len(abbr)