# -*- coding: utf-8 -*-

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """Solver for https://oj.leetcode.com/problems/same-tree/"""
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        """The main solver function."""
        try:
            return (p == q == None) or (p.val == q.val and
                    self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        except AttributeError:
            return False
