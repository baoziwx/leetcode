# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
# #       recursive
#         if root is None:
#             return []
#         else:
#             return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


#       iterative
        if root is None:
            return []

        ret = []
        to_visit = []
        curr = root
        while curr is not None or to_visit != []:
            while curr is not None:
                to_visit += [curr]
                curr = curr.left

            curr = to_visit.pop()
            ret += [curr.val]
            curr = curr.right

        return ret

