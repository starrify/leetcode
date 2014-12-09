# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/triangle/"""
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        """The main solver function."""
        n = len(triangle)
        min_sum = triangle[0]
        for i in xrange(1, n):
            inf = abs(max(min_sum)) + abs(max(triangle[i]))
            tmp = [inf for j in xrange(i + 1)]
            for j in xrange(i + 1):
                if j - 1 >= 0:
                    tmp[j] = min(tmp[j], min_sum[j - 1])
                if j < i:
                    tmp[j] = min(tmp[j], min_sum[j])
                tmp[j] += triangle[i][j]
            min_sum = tmp
        return min(min_sum)
