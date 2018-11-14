# 295. Find Median from Data Stream

from heapq import heappush, heappop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lows = []
        self.highs = []



    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if num > self.findMedian():
            heappush(self.highs, num)
        else:
            heappush(self.lows, -num) # min heap, use negative to have largest value on top

#       balance
        if (len(self.lows) > len(self.highs) + 1): # too many in lows
            to_move = -heappop(self.lows)
            heappush(self.highs, to_move)
        elif (len(self.lows) < len(self.highs)): # too many in highs
            to_move = heappop(self.highs)
            heappush(self.lows, -to_move)


    def findMedian(self):
        """
        :rtype: float
        """
        # print self.lows, self.highs
        # print ''

        if not self.highs:
            return float(-self.lows[0]) if self.lows else None
        if len(self.lows) > len(self.highs):
            return float(-self.lows[0])
        else:
            return float((-self.lows[0] + self.highs[0])) / 2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()