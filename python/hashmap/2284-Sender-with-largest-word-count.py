
# Problem: Leetcode 2284 - Sender with largest word count
# Difficulty: Medium
# Link: https://leetcode.com/problems/sender-with-largest-word-count/description/
# Time Complexity: O(n) - as we go through all the elements to make hashmap and then iterate the hashmap
# Space Complexity: O(n) as we use a hashmap
# Approach: We store the count in hashmap and then iterate it to find the max value and take the keys out that have this value
# then we just sort it and return lexicographically the biggest key


from collections import defaultdict
class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        d = defaultdict(int)
        for i,message in enumerate(messages):
            words = message.split()
            d[senders[i]] += len(words)
        mx = max(d.values())
        ans = []
        for key,value in d.items():
            if value == mx:
                ans.append(key)
        ans.sort()
        return ans[-1]
                