# 755. Pour Water

import sys
class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int -- # of drops
        :type K: int -- fall index
        :rtype: List[int]
        """
        # print max(heights)
        def printHeights(heights):
            for h in range(max(heights), 0, -1):
                for i in range(len(heights)):
                    if heights[i] >= h:
                        sys.stdout.write('#')
                    else:
                        sys.stdout.write(' ')
                print ''

        # printHeights(heights)

        for _ in range(V):
            pos = K
#           try move left
            while pos > 0 and heights[pos - 1] <= heights[pos]:
                # print 'a', pos
                pos -= 1
#           try move right
            while pos < len(heights) - 1 and heights[pos + 1] <= heights[pos]:
                # print 'b', pos
                pos += 1
#           try to move left again back to init pos, if success, then all flat
            while pos > K and heights[pos - 1] <= heights[pos]:
                pos -= 1

            heights[pos] += 1
            # print pos, heights

        # printHeights(heights)

        return heights




