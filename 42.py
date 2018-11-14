# 42. Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftidx = 0
        rightidx = len(height) - 1
        leftmax = 0
        rightmax = 0
        water = 0
        while leftidx < rightidx:
            # print leftidx, rightidx
#           ???
            if height[leftidx] < height[rightidx]:
                if height[leftidx] >= leftmax:
                    leftmax = height[leftidx]
                else:
                    water += leftmax - height[leftidx]
                leftidx += 1
            else:
                if height[rightidx] >= rightmax:
                    rightmax = height[rightidx]
                else:
                    water += rightmax - height[rightidx]
                rightidx -= 1
        return water