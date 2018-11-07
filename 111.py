# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0


        q = [(1, root)]
        while q != []:
            # for l, n in q:
            #     if n is None:
            #         print l, "None"
            #     else:
            #         print l, n.val
            # print ""
            level, node = q[0]
            print level, node
            q = q[1:]
            if node.left is None and node.right is None:
                return level

            if node.left is not None:
                q += [(level + 1, node.left)]
            if node.right is not None:
                q += [(level + 1, node.right)]
            # q += [(level + 1, node.left), (level + 1, node.right)]


