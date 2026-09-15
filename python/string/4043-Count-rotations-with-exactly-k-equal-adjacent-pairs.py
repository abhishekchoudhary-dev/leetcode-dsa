# Problem: Leetcode 4043 - Count rotations with exactly k equal adjacent pairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/description/
# Time Complexity: O(n^2)
# Space Complexity: O(n) in the sense that we generate a new string each time
# Approach - We simple take the total number of rotations and keep rotating the string in a while loop and we calculate
# the score of each rotation and if score is k we increment our count and return it at the end


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        cnt = 0
        rotations = len(s)
        while rotations>0:
            score = 0
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    score+=1
            if score ==k:
                cnt+=1
            s = s[1:] + s[:1]
            rotations-=1
        return cnt