# Problem: Leetcode 4066 - Maximum equal adjacent pairs after at most one replacement
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-one-replacement/description
# Time Complexity: O(n)
# Space Complexity: O(n) as we use hashmap
# Approach: We count pairs that are already same and add the unequal pairs in hashmap and count the most frequent pair which we will match with our one
# available move which shows us the maximum gain we can make. then we return the same pairs pluss the maximum gain we can make


from collections import defaultdict
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        same = 0
        d = defaultdict(int)
        for i in range(len(nums)-1):
            first,second = nums[i],nums[i+1]
            if first == second:
                same+=1
            else:
                key = (min(first,second), max(first,second))
                d[key]+=1
        return same + (max(d.values()) if d else 0)
            
        '''
        if len(set(nums))==1:
            return len(nums)-1
        best = 0
        # freq type array doesnt work as its not limited to characters
        # try window
        left = 0
        d = defaultdict(int)
        for right in range(len(nums)):
            d[nums[right]]+=1
            while left+1<right and len(d)>2:
                d[nums[left]]-=1
                if d[nums[left]]==0:
                    del d[nums[left]]
                left+=1

            best = max(best,right-left+1)

        return best-1
        '''