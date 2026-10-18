# Problem: Leetcode 1768 - Merge string alternately
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-string-alternately/description/
# Time Complexity: O(n) - as we iterate through the string
# Space Complexity: O(n) for our answer array
# Approach: We iterate over the shorter one and keep taking element alternately and then the remaining elements
# from the bigger one is sliced.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        # we can do with cnt
        cnt = 0
        n = len(word1)
        m = len(word2)
        word1 = [char for char in word1]
        word2 = [char for char in word2]
        for i in range(min(m,n)):
            ans.append(word1[i])
            ans.append(word2[i])
            cnt+=1
        if cnt<len(word1):
            ans.extend(word1[cnt:])
        if cnt<len(word2):
            ans.extend(word2[cnt:])
        return ''.join(ans)
        #for i in range(cnt,len(word1)):
        #    ans.append(word1[i])
        #for i in range(cnt,len(word2)):
        #    ans.append(word2[i])
        #return ''.join(ans)