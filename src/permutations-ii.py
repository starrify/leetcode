# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/permutations-ii/"""
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        """The main solver function."""
        # import itertools
        num = sorted(num)
        last_perm = None
        ret = []
        for perm in itertools.permutations(num):
            if not last_perm or perm > last_perm:
                ret += [list(perm)[:]]
                last_perm = perm
        return ret
