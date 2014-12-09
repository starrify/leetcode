# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/maximum-product-subarray/"""
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        """The main solver function."""
        maxpos = A[:]
        minneg = A[:]
        for i in range(1, len(A)):
            maxpos[i] = max(maxpos[i], maxpos[i - 1] * A[i])
            maxpos[i] = max(maxpos[i], minneg[i - 1] * A[i])
            minneg[i] = min(minneg[i], maxpos[i - 1] * A[i])
            minneg[i] = min(minneg[i], minneg[i - 1] * A[i])
        return max(maxpos)
