# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/valid-palindrome/"""
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        """The main solver function."""
        tmp = ''.join(x if x.isalnum() else '' for x in s).lower()
        return tmp == tmp[::-1]
