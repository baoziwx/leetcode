# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterative
        tail = None
        curr = None
        while head:
            # print head.val
            # print curr.val if curr else "None"
            # print tail.val if tail else "None"
            # print ""
            curr = head
            head = head.next

            curr.next = tail
            tail = curr
            # print head
        return curr

        # recursive


