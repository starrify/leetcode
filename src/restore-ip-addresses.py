# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/restore-ip-addresses/"""
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        """The main solver function."""
        ret = []
        # import itertools
        for prod in itertools.product((1, 2, 3), repeat=3):
            tmp_s = s
            tmp_ip = []
            for i in prod:
                tmp_ip += [tmp_s[:i]]
                tmp_s = tmp_s[i:]
            tmp_ip += [tmp_s]
            if all(self._check_ip_digit(x) for x in tmp_ip):
                ret += ['.'.join(tmp_ip)]
        return ret

    @staticmethod
    def _check_ip_digit(s):
        return s and (len(s) == 1 or s[0] != '0') and int(s) < 256
