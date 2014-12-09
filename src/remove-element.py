# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/remove-element/"""
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        """The main solver function."""
        revindex = len(A) - 1
        index = 0
        while True:
            while revindex >= 0 and A[revindex] == elem:
                revindex -= 1
            if revindex < 0:
                return 0
            while index < len(A) and A[index] != elem:
                index += 1
            if index == len(A):
                return len(A)
            if revindex < index:
                return index
            tmp = A[revindex]
            A[revindex] = A[index]
            A[index] = tmp
