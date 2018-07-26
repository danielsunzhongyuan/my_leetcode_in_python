# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        paths = []
        self.dfs(paths, [], root)
        res = 0
        for path in paths:
            tmp = 0
            for i in path:
                tmp = tmp*10 + i
            res += tmp
        return res
        
    def dfs(self, paths, prefix, node):
        if not node.left and not node.right:
            prefix.append(node.val)
            paths.append([x for x in prefix])
        if node.left:
            self.dfs(paths, prefix + [node.val], node.left)
        if node.right:
            self.dfs(paths, prefix + [node.val], node.right)
