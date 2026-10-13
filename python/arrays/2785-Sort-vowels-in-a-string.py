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
# we only get the sorted order.

class Solution:
    def sortVowels(self, s: str) -> str:
        '''
        #simple method - O(n log n) and O(2n)
        vowels = 'aeiouAEIOU'
        indices = []
        vow = []
        for i,char in enumerate(s):
            if char in vowels:
                indices.append(s)
                vow.append(char)
        vow.sort()
        j = 0
        s = [char for char in s]
        for i,char in enumerate(s):
            if char in vowels:
                s[i] = vow[j]
                j+=1
        return ''.join(s)
        '''
        #counting sort - O(n)
        vowels = 'AEIOUaeiou'
        freq_array = [0]*100
        for char in s:
            if char in vowels:
                freq_array[ord(char)-ord('A')]+=1
        ans = []
        #print(freq_array)
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                while j< len(vowels) and freq_array[ord(vowels[j])-ord('A')]==0:
                    j+=1
                ans.append(vowels[j])
                freq_array[ord(vowels[j])-ord('A')]-=1
            else:
                ans.append(s[i])

        return ''.join(ans)