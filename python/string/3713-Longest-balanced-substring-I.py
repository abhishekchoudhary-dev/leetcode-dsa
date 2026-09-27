# Problem: Leetcode 3713 - Longest balanced substring I
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-balanced-substring/description/
# Time Complexity: O(n^2) as we loop through the string 
# Space Complexity: O(1) as we only use only fixed size small array and pointers
# Approach: For each starting index we we initialize a freq array where we count how many uniqye characters we have seen
# and mx tracks the max freq of any of the characters. Then for each j main job is done by the formula
# if mx*v == j-i+1 which checks that the mx freq multiplied by the number of unique characters is actually equal to the length of the substring
# If yes then that means all characters have the same frequency and we can update best for the current substring length. 
# at the end we return best.


class Solution:
    def longestBalanced(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            cnt = [0]*26
            mx = v = 0
            for j in range(i, len(s)):
                c = ord(s[j])-ord('a')
                cnt[c]+=1
                if cnt[c]==1:
                    v+=1
                mx = max(mx,cnt[c])
                if mx*v == j-i+1:
                    best = max(best,j-i+1)
        return best
        '''brute force O(n^3) fails
        best = 1
        seen = set()
        d = {0:-1}
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                sub = s[i:j+1]
                d = Counter(sub)
                vals = [v for v in d.values()]
                if len(set(vals)) == 1:
                    best = max(best, len(sub))
        return best
        '''
        