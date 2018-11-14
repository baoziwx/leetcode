# 11. Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxA = current = 0
        while left < right:
            current = min(height[left], height[right]) * (right - left)
            maxA = max(maxA, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA