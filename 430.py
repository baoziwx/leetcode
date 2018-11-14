"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        curr = head
        while curr:
            if curr.child:
#               push next to stack if not end-of-list
                if curr.next:
                    stack.append(curr.next)

#               connect child as next
                child = curr.child
                curr.child = None
                curr.next = child
                child.prev = curr

            elif not curr.next and stack:
#               at end of list, reconnect to next at previous level
                curr.next = stack.pop()
                curr.next.prev = curr

#           nothing special, increment
            curr = curr.next

        return head
