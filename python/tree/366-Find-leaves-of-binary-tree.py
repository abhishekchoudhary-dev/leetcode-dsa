# Problem: Leetcode 366 - Find leaves of binary tre
# Difficulty: Medium
# Link: https://leetcode.com/find-leaves-of-binary-tree/description/
# Time Complexity: O(n) as we go deep in tree
# Space Complexity: O(1)
# Approach: We first calculate the height at each level by doing dfs on both sides and then we take h 
# and if h found at a depth is equal to the len of ans right now. Then we just keep adding node values at the current height level as we have to collect them for the lowest height
# to the maximum height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        def dfs(node):
            if not node:
                return -1
            h = 1+max(dfs(node.left),dfs(node.right))
            if h == len(ans):
                ans.append([])
            ans[h].append(node.val)
            return h
        ans = []
        dfs(root)
        return ans