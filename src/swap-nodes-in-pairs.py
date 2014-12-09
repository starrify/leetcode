# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """Solver for https://oj.leetcode.com/problems/swap-nodes-in-pairs/"""
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        """The main solver function."""
        tmp = head
        head = ListNode(0)
        head.next = tmp
        tmp = head
        while tmp.next and tmp.next.next:
            swap = tmp.next
            tmp.next = swap.next
            swap.next = tmp.next.next
            tmp.next.next = swap
            tmp = tmp.next.next
        return head.next
