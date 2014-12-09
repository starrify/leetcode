# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/decode-ways/"""
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        """The main solver function."""
        if not s:
            return 0
        nums = [str(i) for i in range(1, 26 + 1)]
        ans = [0 if i else 1 for i in range(len(s) + 1)]
        for i in range(len(s)):
            for num in nums:
                if i + len(num) <= len(s):
                    if s[i:][:len(num)] == num:
                        ans[i + len(num)] += ans[i]
        return ans[len(s)]
