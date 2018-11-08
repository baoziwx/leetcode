# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None:
            return False
        # if head.next.next is None:
        #     return head == head.next

        slow = head
        fast = head.next
        while (slow <> fast):
            if slow is None or fast is None or fast.next is None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True