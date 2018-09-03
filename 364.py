# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        thisDepth = [1]
        maxDepth = [1]
        self.findMaxDepth(nestedList, thisDepth, maxDepth)
        print maxDepth
        totalSum = [0]
        depth = [1]
        self.depthSumInverseHelper(nestedList, totalSum, depth, maxDepth[0])

        return totalSum[0]

    def findMaxDepth(self, nestedList, thisDepth, maxDepth):
        hasList = False
        for n in nestedList:
            if not n.isInteger():
                print n
                hasList = True
                thisDepth[0] += 1
                self.findMaxDepth(n.getList(), thisDepth, maxDepth)
                thisDepth[0] -= 1
            # else:
            #     print n.getInteger()
            #     print thisDepth

        if not hasList:
            maxDepth[0] = max(thisDepth[0], maxDepth[0])

    def depthSumInverseHelper(self, nestedList, totalSum, depth, maxDepth):
        for n in nestedList:
            if n.isInteger():
                # print depth[0]
                totalSum[0] += (maxDepth - depth[0] + 1) * n.getInteger()
            else:
                depth[0] += 1
                self.depthSumInverseHelper(n.getList(), totalSum, depth, maxDepth)
                depth[0] -= 1
