# Problem: Leetcode 824 - Goat latin
# Difficulty: Easy
# Link: https://leetcode.com/problems/goat-latin/description/
# Time Complexity: O(n) as we iterate over string
# Space Complexity: O(n) as we make a list by splitting the sentence
# Approach: We simply loop the words in the array and if it starts with a wovel we add ma and "a"*(i+1) and if it starts 
# with a consonant we first slice the string and addd the first alphabet at the end and then add the 'ma' and 'a'.
# we return the array after modifying each element independenty in the form of a string.

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        print(words)
        for i in range(len(words)):
            if words[i].lower()[0] in ('a','e','i','o','u'):
                words[i] = words[i] + "ma" + "a"*(i+1)
            else:
                words[i] = ''.join(words[i][1:])+ words[i][0]+"ma"+"a"*(i+1)
        return ' '.join(words)