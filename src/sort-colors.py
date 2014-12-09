# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/sort-colors/"""
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        """The main solver function."""
        count = [0 for i in range(3)]
        for value in A:
            count[value] += 1
        A[:] = sum(([key] * value for key, value in enumerate(count)), [])
        return
