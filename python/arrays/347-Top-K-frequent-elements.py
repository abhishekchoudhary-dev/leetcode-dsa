# Problem: Leetcode 347 - Top K frequent elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: We simple make hashmap and make a sorted list of hashmap keys in reverse order(most to least frequent)
# based on the freq of those keys. Then we just take the first k keys and return them

from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = Counter(nums)
        s = sorted(d.items(), key=lambda x:x[1], reverse = True)
        return [e[0] for e in s[:k]]
        '''
        # make answer with while loop
        ans = []
        while k > 0:
            ans.append(s[k-1][0])
            k-=1
        return ans
        '''