# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """Solver for https://oj.leetcode.com/problems/partition-list/"""
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        """The main solver function."""
        head_0 = ListNode(-1)
        tail_0 = head_0
        head_1 = ListNode(-1)
        tail_1 = head_1
        while head:
            tmp = head.next
            head.next = None
            if head.val < x:
                tail_0.next = head
                tail_0 = head
            else:
                tail_1.next = head
                tail_1 = head
            head = tmp
        tail_0.next = head_1.next
        return head_0.next
