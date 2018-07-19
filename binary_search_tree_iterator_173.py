# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorderStack = []
        self.root = root
        self.resetIterator(self.root)

    def resetIterator(self, root):
        self.inorderStack = []
        cur = root
        if cur != None:
            self.inorderStack.append(cur)
            cur = cur.left
        while cur != None:
            self.inorderStack.append(cur)
            cur = cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.inorderStack:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        res = self.inorderStack.pop()
        cur = res.right
        while cur:
            self.inorderStack.append (cur)
            cur = cur.left
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
