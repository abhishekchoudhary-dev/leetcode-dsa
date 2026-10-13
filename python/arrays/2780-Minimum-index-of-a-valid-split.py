# Problem: Leetcode 2780 - Minimum index of a valid split
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-index-of-valid-split/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: Minimum index of a valid split

from typing import List
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = Counter(nums)
        number = max(d,key=d.get)
        total = d[number]
        n = len(nums)
        cnt = 0
        for i,num in enumerate(nums):
            if num==number:
                cnt+=1
                if cnt > (i+1)//2:
                    rem = n - i -1
                    rem_dominant= total - cnt
                    if rem_dominant>rem//2:
                        return i
        return -1
        '''
                if i%2==1 and cnt >= (i+1)//2 + 1:
                    rem = n - i -1
                    rem_d = total-cnt
                    if (rem%2==1 and rem_d>= (rem)//2+1) or (rem%2==0 and rem_d>rem//2):
                        return i
            
                elif i%2==0 and cnt>i//2:
                    rem = n - i -1
                    rem_d = total - cnt
                    if (rem%2==1 and rem_d>=(rem)//2+1) or (rem%2==0 and rem_d>rem//2):
                        return i
    

        return -1
        '''
            