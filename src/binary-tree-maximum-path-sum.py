# -*- coding: utf-8 -*-

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """Solver for https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/"""
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        """The main solver function."""
        if root is None:
            return 0
        self.maxPathSum(root.left)
        self.maxPathSum(root.right)
        # Max sum of path that ends at root
        max_sum_0 = 0
        # Max sum of path inside tree
        max_sum_1 = float('-inf')
        # Max sum of path that includes the root
        max_sum_2 = 0
        if root.left:
            max_sum_0 = max(max_sum_0, root.left._max_sum_0)
            max_sum_1 = max(max_sum_1, root.left._max_sum_1)
            max_sum_2 += max(0, root.left._max_sum_0)
        if root.right:
            max_sum_0 = max(max_sum_0, root.right._max_sum_0)
            max_sum_1 = max(max_sum_1, root.right._max_sum_1)
            max_sum_2 += max(0, root.right._max_sum_0)
        max_sum_0 += root.val
        max_sum_2 += root.val
        max_sum_1 = max(max_sum_1, max_sum_2)
        setattr(root, '_max_sum_0', max_sum_0)
        setattr(root, '_max_sum_1', max_sum_1)
        return max_sum_1
