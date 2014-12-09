# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/divide-two-integers/"""
    # @return an integer
    def divide(self, dividend, divisor):
        """The main solver function."""
        nega = 0
        nega ^= dividend < 0
        dividend = abs(dividend)
        nega ^= divisor < 0
        divisor = abs(divisor)
        remainder = 0
        exp = 1
        while divisor << 1 < dividend:
            divisor <<= 1
            exp <<= 1
        while dividend and divisor:
            while dividend >= divisor:
                dividend -= divisor
                remainder += exp
            while dividend < divisor:
                divisor >>= 1
                exp >>= 1
        if nega:
            remainder = -remainder
        MAX_INT = 2 ** 31 - 1
        if remainder > MAX_INT:
            remainder = MAX_INT
        if remainder < -MAX_INT - 1:
            remainder = -MAX_INT - 1
        return remainder
