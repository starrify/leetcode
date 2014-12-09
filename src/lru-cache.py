# -*- coding: utf-8 -*-

class LRUCache(object):
    """Solver for https://oj.leetcode.com/problems/divide-two-integers/"""

    class DList(object):
        """Double linked list."""
        key = None
        val = None
        prec = None
        succ = None

    # @param capacity, an integer
    def __init__(self, capacity):
        """Initializes the cache."""
        self._cache_dict = {}
        self._cache_head = self.DList()
        self._cache_tail = self.DList()
        self._cache_head.succ = self._cache_tail
        self._cache_tail.prec = self._cache_head
        self._size = 0
        self._capacity = capacity

    def update_key(self, key):
        """Updates key in cache."""
        node = self._cache_dict[key]
        node.prec.succ = node.succ
        node.succ.prec = node.prec
        node.prec = self._cache_head
        node.succ = self._cache_head.succ
        node.succ.prec = node
        self._cache_head.succ = node

    # @return an integer
    def get(self, key):
        """Gets item from cache."""
        if key in self._cache_dict:
            self.update_key(key)
            return self._cache_dict[key].val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        """Sets item to cache."""
        if key in self._cache_dict:
            # Update
            self.update_key(key)
            self._cache_dict[key].val = value
        else:
            # Insert
            self._size += 1
            node = self.DList()
            node.key = key
            node.val = value
            node.prec = self._cache_head
            node.succ = self._cache_head.succ
            node.succ.prec = node
            self._cache_head.succ = node
            self._cache_dict[key] = node
            if self._size > self._capacity:
                node = self._cache_tail.prec
                self._cache_tail.prec = node.prec
                node.prec.succ = self._cache_tail
                self._cache_dict.pop(node.key)
                self._size -= 1
