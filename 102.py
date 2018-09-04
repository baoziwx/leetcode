# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []

        r = {}
        # r[0] = [root.val]
        depth = 0

        def levelOrderHelper(root, r, depth):
            if root is None:
                return
            else:
                levelOrderHelper(root.left, r, depth + 1)
                r[depth] = r.get(depth, []) + [root.val]
                levelOrderHelper(root.right, r, depth + 1)

        levelOrderHelper(root, r, depth)
        return r.values()