# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#       key = level, val = node
        rightmost = {}
        to_visit = deque([(root, 0)])
        max_lv = -1
        while to_visit:
            node, level = to_visit.popleft()
            if node is not None:
                max_lv = level
                rightmost[level] = node.val
                to_visit.append((node.left, level + 1))
                to_visit.append((node.right, level + 1))
        # print max_lv
        # print rightmost
        output = []
        for i in range(max_lv + 1):
            output.append(rightmost[i])

        return output


