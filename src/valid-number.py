# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/valid-number/"""
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        """The main solver function."""
        try:
            tmp = float(s)
            return True
        except:
            return False
