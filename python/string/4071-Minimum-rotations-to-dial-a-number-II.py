# Problem: Leetcode 4070 - Minimum rotations to dial a number II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-rotations-to-dial-a-number-II/description/
# Time Complexity: O(n) - as we iterate on the string 
# Space Complexity: O(1) as we only have a few pointers
# Approach: So we calculate the total rotations of default string and also calculate the maximum gain we can have(reducing the rotations by max possible) 
# at each index by comparing rotations from previous index and with last string element(assuming string was rotated at this index). 
# At end end we can just return the usual score minus the max gain we can take.


class Solution:
    def minRotations(self, n: int, s: str) -> int:
        prev = 0
        mx_gain = 0
        #rot = min(int(s[0]),10-int(s[0]))
        rot = 0
        #target_idx = None
        for i in range(len(s)):
            #val = abs(int(s[i])- int(s[i-1]))
            val = abs(int(s[i])- prev)
            rot+= min(val,10-val)
            if min(abs(int(s[i]) - prev), 10 - (abs(int(s[i]) - prev))) > min(abs(int(s[-1])-prev),10-(abs(int(s[-1])-prev))):
                current = min(abs(int(s[i]) - prev), 10 - (abs(int(s[i]) - prev)))
                rotated = min(abs(int(s[-1])-prev),10-(abs(int(s[-1])-prev)))
                gain = current - rotated
                if gain>mx_gain:
                    mx_gain = gain
                    #target_idx = i
            prev = int(s[i])
        # now rotate as per target idx
        #if target_idx is not None:
        #    s = s[:target_idx] + s[target_idx:][::-1]
        # now ready to calculate rotation
        #rot = min(int(s[0]),10-int(s[0])) #start value
        #calculate rotations
        #for i in range(1,n):
        #    val = abs(int(s[i])- int(s[i-1]))
        #    rot+=min(val,10-val)
        return rot - mx_gain