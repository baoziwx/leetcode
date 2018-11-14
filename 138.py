# 138. Copy List with Random Pointer

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        old_new_map = {}
        old_new_map[None] = None
        curr = head
        while curr:
            new = RandomListNode(curr.label)
            old_new_map[curr] = new
            curr = curr.next

        curr = head
        while curr:
            old_new_map[curr].next = old_new_map[curr.next]
            old_new_map[curr].random = old_new_map[curr.random]
            curr = curr.next

        return old_new_map[head]