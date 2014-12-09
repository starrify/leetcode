# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/pascals-triangle-ii/"""
    # @return a list of integers
    def getRow(self, rowIndex):
        """The main solver function."""
        row = [1]
        for n in range(1, rowIndex + 1):
            tmp_0 = [0] + row
            tmp_1 = row + [0]
            row = [tmp_0[i] + tmp_1[i] for i in range(n + 1)]
        return row
