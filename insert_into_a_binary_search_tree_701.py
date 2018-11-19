# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if cur.val <= val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
        return root
