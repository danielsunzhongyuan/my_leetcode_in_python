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
        if not root:
            return True
        q = []
        if (root.left and not root.right) or (root.right and not root.left):
            return False
        if not root.left and not root.right:
            return True
        q.append(root.left)
        q.append(root.right)
        while q:
            node2, node1 = q.pop(), q.pop()
            if node1.val != node2.val:
                return False
            if (node1.left and not node2.right) or (not node1.left and node2.right) or (node1.right and not node2.left) or (not node1.right and node2.left):
                return False
            if node1.left and node2.right:
                q.append(node1.left)
                q.append(node2.right)
            if node1.right and node2.left:
                q.append(node1.right)
                q.append(node2.left)
        return True
