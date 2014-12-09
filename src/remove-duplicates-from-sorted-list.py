# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """Solver for https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/"""
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        """The main solver function."""
        new_head = ListNode(0)
        new_tail = new_head
        tmp = head
        while tmp:
            if tmp.val == new_tail.val and new_tail != new_head:
                tmp = tmp.next
            else:
                new_tail.next = tmp
                tmp = tmp.next
                new_tail = new_tail.next
                new_tail.next = None
        return new_head.next
