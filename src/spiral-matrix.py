# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/spiral-matrix/"""
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        """The main solver function."""
        ret = []
        # import copy
        tmp = copy.deepcopy(matrix)
        mode = 0
        while tmp and tmp[0]:
            if mode == 0:
                ret += tmp[0]
                tmp = tmp[1:]
            elif mode == 1:
                ret += [x[-1] for x in tmp]
                tmp = [x[:-1] for x in tmp]
            elif mode == 2:
                ret += tmp[-1][::-1]
                tmp = tmp[:-1]
            elif mode == 3:
                ret += [x[0] for x in tmp][::-1]
                tmp = [x[1:] for x in tmp]
            else:
                raise ValueError
            mode += 1
            mode %= 4
        return ret
