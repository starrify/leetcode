# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/trapping-rain-water/"""
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        """The main solver function."""
        forward_max = self.scan(A, max)
        backward_max = self.scan(A[::-1], max)[::-1]
        ret = 0
        for i in range(len(A)):
            wlevel = min(forward_max[i], backward_max[i])
            ret += wlevel - A[i]
        return ret

    @staticmethod
    def scan(seq, op):
        """Perform a prefix scan in the naive way."""
        ret = seq[:]
        for i in range(1, len(seq)):
            ret[i] = op(ret[i - 1], ret[i])
        return ret
