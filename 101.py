# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True

        def isSymmetricHelper(left, right):
            if left is None and right is None:
                return True
            elif left is None and not right is None:
                return False
            elif not left is None and right is None:
                return False
            else: #both not none
                return left.val == right.val and isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)


        return isSymmetricHelper(root.left, root.right)