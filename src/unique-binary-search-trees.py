# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/unique-binary-search-trees/"""
    # @return an integer
    def numTrees(self, n):
        """The main solver function."""
        ans = [0 if i > 0 else 1 for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                ans[i] += ans[j] * ans[i - 1 - j]
        return ans[n]
