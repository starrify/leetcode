# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/add-binary/"""
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        """The main solver function."""
        return bin(int(a, 2) + int(b, 2))[2:]
