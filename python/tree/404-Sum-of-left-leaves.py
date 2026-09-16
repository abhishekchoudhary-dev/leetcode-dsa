# Problem: Leetcode 404 - Sum of left leaves
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-left-leaves/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(1) as we only use variable to sum up the values
# Approach: We go dfs in the tree and at each step we check if the node has a left node and that left node is actually a leaf.
# If it is a leaf then we add its value to total. If its not then we go deeper into left side. else we dont keep deeper on the branch
# and out of the left branch we always to dfs on node.right to check its left branch later on

from typing import Optional,List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        def dfs(node):
            nonlocal total
            if not node:
                return 
            #if node.left exists but no children then dont recurse into it.
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val
            else:
                # else we recurse
                dfs(node.left)
            dfs(node.right) #right side we always recurse

        total = 0
        dfs(root)
        return total