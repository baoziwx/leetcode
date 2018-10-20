class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, n):
        if n is not None:
            prev = n.prev
            next = n.next
            prev.next = next
            next.prev = prev


    def add(self, n):
        if n is not None:
            tmp = self.head.next
            self.head.next = n
            tmp.prev = n
            n.prev = self.head
            n.next = tmp

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print 'get'
        # print key
        # print self.dict.keys()
        if not key in self.dict:
            # print key
            return -1

        # key exists
        node = self.dict[key]

        # first remove node
        self.remove(node)

        # then add node to top of list
        self.add(node)

        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print 'put' + str(key) + ',' + str(value)
        # print self.dict.keys()

        if key in self.dict:
            # node = self.dict[key]
            self.remove(self.dict[key])

        node = Node(key, value)

        self.dict[key] = node

        #put node at top of list
        self.add(node)

        #if already full remove last element
        if (len(self.dict) > self.capacity):
            toDel = self.tail.prev
            self.dict.pop(toDel.key, None)
            self.remove(toDel)
            # tmp = self.tail.prev
            # if tmp is not None and tmp.prev is not None:
            # print tmp
            # print self.tail
            # print self.head
            # print self.capacity
            # print len(self.dict)
            # print self.dict
            # print self.dict.keys()
            # print tmp.prev
            # tmp.prev.next = self.tail
        # print self.dict.keys()

        # debug
        # n = self.head.next
        # while not n is None and not n == self.tail:
        #     print n
        #     n = n.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)