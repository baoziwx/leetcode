# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def countLen(l):
            length = 0
            curr = l
            while not curr is None:
                length += 1
                curr = curr.next
            return length


        ret = ListNode(0)
        curr = ret

        len1 = countLen(l1)
        len2 = countLen(l2)
        if len1 > len2:
            longer, shorter, longerLen = l1, l2, len1
        else:
            longer, shorter, longerLen = l2, l1, len2

        # longer, shorter = l1, l2 if len1 > len2 else l2, l1
        # print longerLen, shorterLen
        # print ''
        # for i in range(longerLen - shorterLen):
        #     print i
        #     curr = curr.next
        #     curr = ListNode(longer.val)
        #     longer = longer.next

        print ''
        carry = 0
        for i in range(longerLen):
            # print i
            # print ret
            # print curr
            # curr = curr.next
            sum = longer.val + shorter.val + carry if not shorter is None else longer.val + carry
            print longer.val, shorter.val if not shorter is None else 'null', carry, sum
            if sum >= 10:
                curr.next = ListNode(sum - 10)
                carry = 1 #max carry is 1 for addition
            else:
                curr.next = ListNode(sum)
                carry = 0

            longer = longer.next
            if not shorter is None: shorter = shorter.next
            curr = curr.next

        if carry == 1: curr.next = ListNode(1)

        # q = ret
        # while not q is None:
        #     print q
        #     q = q.next

        return ret.next


