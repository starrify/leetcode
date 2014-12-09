# -*- coding: utf-8 -*-

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """Solver for https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/"""
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        """The main solver function."""
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
