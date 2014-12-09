# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/jump-game-ii/"""
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        """The main solver function."""
        inf = len(A)
        min_step = [inf if i else 0 for i in xrange(len(A))]
        for loc, max_step in enumerate(A):
            for step in xrange(max_step, 0, -1):
                target_loc = loc + step
                if target_loc < len(A):
                    if min_step[target_loc] > min_step[loc] + 1:
                        min_step[target_loc] = min_step[loc] + 1
                    else:
                        break
        return min_step[-1]
