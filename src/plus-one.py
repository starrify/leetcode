# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/plus-one/"""
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        """The main solver function."""
        digits = digits[::-1] + [0]
        digits[0] += 1
        for i in range(len(digits) - 1):
            digits[i + 1] += digits[i] / 10
            digits[i] %= 10
        digits = digits[::-1]
        while digits[0] == 0:
            digits = digits[1:]
        return digits
