# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/median-of-two-sorted-arrays/"""
    # @return a float
    def findMedianSortedArrays(self, A, B):
        """The main solver function."""
        midindex_0 = (len(A) + len(B) - 1) / 2
        midindex_1 = (len(A) + len(B)) / 2
        if midindex_0 == midindex_1:
            return self._nthmin(midindex_0, A, B)
        else:
            return (
                self._nthmin(midindex_0, A, B)
                + self._nthmin(midindex_1, A, B)) / 2.0

    @staticmethod
    def _nthmin(n, A, B):
        """Returns nth(0-indexed) minimum element of sorted arrays A and B."""
        if not A:
            return B[n]
        if not B:
            return A[n]
        if n == 0:
            return min(A[0], B[0])
        nexclude = (n + 1) / 2
        nexA = min(nexclude, len(A))
        nexB = min(nexclude, len(B))
        if A[nexA - 1] < B[nexB - 1]:
            return Solution._nthmin(n - nexA, A[nexA:], B)
        else:
            return Solution._nthmin(n - nexB, A, B[nexB:])
