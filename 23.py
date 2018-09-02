# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        q = []
        r = curr = ListNode(0)
        for l in lists:
            while l is not None:
                heappush(q, (l.val, l));
                l = l.next

        while q != []:
            curr.next = ListNode(heappop(q)[0])
            curr = curr.next


        return r.next

#         # print lists
#         # return
#         result = current = ListNode(0)
#         done = False
#         toCompare = map(lambda l: l, lists)
#         # hasNonEmptyList = False
#         while not done:
#             # hasNonEmptyList = False
#             # currentMinIdx = 0
#             # currentMin = lists[currentMinIdx]

#             currentMin = max(lists, key=lambda n: n.val if n is not None else None)
# # #           loop through list and find current min
# #             for idx, l in enumerate(lists):
# #                 if l is not None:
# #                     # hasNonEmptyList = True
# #                     # print l
# #                     # print currentLargest
# #                     if (currentMin is None and l is not None) or l.val < currentMin.val:
# #                         currentMin = l
# #                         currentMinIdx = idx
# #           set current min to next node
#             current.next = currentMin

# #           if not at end of list, move to next
#             if currentMin is not None:
#                 lists[currentMinIdx] = currentMin.next

#             current = current.next

#                 # print result
#             done = current is None
#         return result.next

