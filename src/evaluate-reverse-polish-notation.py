# -*- coding: utf-8 -*-

class Solution:
    """Solver for https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/"""
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        """The main solver function."""
        values = []
        # import operator
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a * 1.0 / b),
            }
        for token in tokens:
            if token in operators:
                operand_1 = values.pop()
                operand_0 = values.pop()
                result = operators[token](operand_0, operand_1)
                values.append(result)
            else:
                values.append(int(token))
        return values[0]
