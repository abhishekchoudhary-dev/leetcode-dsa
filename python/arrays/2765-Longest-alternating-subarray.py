
# Problem: Leetcode 2765 - Longest alternating subarray
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-alternating-subarray/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach2: We have brute force O(n^3) where we check all subarrays and check if they are alternating and take the max lengt with j-i+1
# Approach1: We devise and O(n) solution where we just inSeq flag and a parity flag to check if a diffenrece of 1 starts a new sequence of extends previous one
# and similarly if a difference of -1 extends a previous sequence or not. Any other difference which is not 1 or -1 definitely break the sequence
# and we reset our flags and the parity to find a new sequence.

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        vowels = ('a','e','i','o','u')
        for idx,word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels and idx>=left and idx<=right:
                cnt +=1
        return cnt

from typing import List
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        
        
        best = -1
        alter = 1
        inSeq = False
        parity = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i]==1:
                if inSeq and parity%2==0:
                    alter+=1
                    parity = 1
                else:
                    alter = 2 # start a new sequence
                    parity = 1
                    inSeq= True
            elif nums[i+1] - nums[i]==-1:
                if inSeq and parity%2==1:
                    alter+=1
                    parity=0
                else:
                    inSeq = False
                    alter = 1
                    parity = 0
            else:
                inSeq = False
                alter=1
                parity=0

            #print("alter at index",i,"is",alter)
            best = max(best,alter)
        return best if best>1 else -1
        

        '''
        #brute force
        def is_alternating(arr):
            for i in range(len(arr)-1):
                if i%2==0:
                    if arr[i+1] - arr[i]!=1:
                        return False
                elif i%2==1:
                    if arr[i+1]-arr[i]!=-1:
                        return False
            return True
        best = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sub = nums[i:j+1]
                if is_alternating(sub):
                    best = max(best,j-i+1)

        return best
        '''