# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/find-peak-element/"""
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        """The main solver function."""
        return self._bsearch(0, len(num) - 1, num)
    
    @staticmethod
    def _bsearch(l, r, num):
        """Performs a binary search on the given range and find a peak."""
        if l == r:
            return l
        mid = (l + r) / 2
        assert mid < r
        if num[mid + 1] > num[mid]:
            return Solution._bsearch(mid + 1, r, num)
        else:
            return Solution._bsearch(l, mid, num)
