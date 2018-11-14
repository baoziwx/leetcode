# 378 Kth Smallest Element in a Sorted Matrix

from heapq import heappush, heappop

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        n  = len(matrix)
        for i in range(n):
            for j in range(n):
                heappush(heap, matrix[i][j])

        for i in range(k - 1):
            heappop(heap)

        return heappop(heap)
