# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        needRemove = self.needRemove(root)
        if needRemove:
            return None
        else:
            return root
        
    def needRemove(self, node):
        if node.val == 0 and not node.left and not node.right:
            return True
        leftNeedRemove = True
        rightNeedRemove = True
        if node.left:
            leftNeedRemove = self.needRemove(node.left)
            if leftNeedRemove:
                node.left = None
        if node.right:
            rightNeedRemove = self.needRemove(node.right)
            if rightNeedRemove:
                node.right = None
        if node.val == 0 and not node.left and not node.right:
            return True
        else:
            return False
        
