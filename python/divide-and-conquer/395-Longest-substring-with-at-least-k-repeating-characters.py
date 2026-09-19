# Problem: Leetcode 395 - Longest substring with at least k repeating characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Dp and sliding windows dont work as there is no monotonicity. So we do divide and conquer where we do a recursive loop
# on splitted parts of the string and then check if all characters have the desired frequency. Each recursive element return the length of the string 
# if its successful and this value bubbles up the stack.

from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        d = Counter(s)
        for char,freq in d.items():
            if freq < k:
                return max((self.longestSubstring(piece,k) for piece in s.split(char)))
        return len(s)
        '''
        brute force passed but TLE
        mx = 0
        for i in range(len(s)):
            for j in range(len(s)):
                d = Counter(s[i:j+1])
                if all(val>=k for val in d.values()):
                    mx = max(mx,j-i+1)
        return mx
        '''

        '''
        left = 0
        start = 0
        ans = 0
        dp = [0]*(len(s)+1)
        d = defaultdict(int)
        for right in range(len(s)):
            d[s[right]]+=1
            if d[s[right]]>=k:
                dp[right+1] = max(dp[right], right+1)
    
            ans = max(ans,dp[right+1])
        print(dp)
        return ans
        '''
            