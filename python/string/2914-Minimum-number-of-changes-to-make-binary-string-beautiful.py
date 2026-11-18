# Problem: Leetcode 2914 - Minimum number of changes to make binary string beautiful
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/
# Time Complexity: O(n)
# Space Complexity: O(n) 
# Approach: We iterate over the string keeping count of a run and keep checking if the current character is equal to the previous one
# if not then we we check the run count. If previous run is odd then we need to change the current character else no. So if ye
# we change the current character by incrementing count and setting run to 0 now as next character will start a new run
# other if they are unequal but previous run is even then we just reset run to 1 as new run now starts with current character and not with next one
# Approach2: one crazy optimization is that we need to observe that at the end all the broken down pairs will be same when string will be fixed.
# so we can just iterate in pairs and check how many pairs are unequal and return that cnt



class Solution:
    def minChanges(self, s: str) -> int:
        #pair counting method
        cnt = 0
        for i in range(0,len(s)-1,2):
            if s[i]!=s[i+1]:
                cnt+=1
        return cnt #you can reduce iterations by half
        '''
        cnt = 0
        run = 1
        #s = [char for char in s]
        n = len(s)
        #for i,ch in enumerate(s[1:],1):
        for i in range(1,n):
            if s[i]!=s[i-1] and run%2==1:
                #s[i] = s[i-1]
                cnt+=1
                run=0
            elif s[i]!=s[i-1]:
                run = 1
            else:
                run+=1
        return cnt
        '''
        
