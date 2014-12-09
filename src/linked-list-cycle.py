# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """Solver for https://oj.leetcode.com/problems/linked-list-cycle/"""
    # @param head, a ListNode
    # @return a list node
    def hasCycle(self, head):
        """The main solver function."""
        fast = head
        slow = head
        while True:
            try:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
                pass
            except AttributeError:
                return False
