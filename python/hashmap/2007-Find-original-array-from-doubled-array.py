# Problem: Leetcode 2007 - Find original array from doubled array
# Difficulty: Medium
# Link: https://leetcode.com/problems/finding-original-array-from-doubled-array/description/
# Time Complexity: O(n) - as we count frequencies and iterate over it
# Space Complexity: O(n) as we use a hashmap
# Approach: Important question to learn since I forgot about keeping freq with hashmap. General hashmap or set does not work
# as there is repetition so set cannot track and hashmap key value get overwritten. so only way is to keep freq
# in hashmap keys and to keep updating it

class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed)%2==1:
            return []
       
        #hashmap fails due to repetition in the array
        #dual side mapping
        d = {}
        d_to_s = {}
        changed.sort()
        for i in range(len(changed)):
            d[changed[i]] = d.get(changed[i],0)+1
        original = [0] * (len(changed)//2)
        write = 0
        for num in changed:
            if num in d and d[num]>0:
                d[num]-=1
                twice = num*2
                if twice in d and d[twice]>0:
                    d[twice]-=1
                    original[write] = num
                    write+=1
                else:
                    return []
        return original