# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """Solver for https://oj.leetcode.com/problems/linked-list-cycle-ii/"""
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        """The main solver function."""
        tmp = head
        while tmp:
            if hasattr(tmp, '_visited'):
                return tmp
            setattr(tmp, '_visited', True)
            tmp = tmp.next
        return None
