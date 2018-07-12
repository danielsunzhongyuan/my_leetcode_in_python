# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = {}
        if not root:
            return []
        def traversal(root, res):
            if root is None:
                return
            res[root.val] = res.get(root.val, 0) + 1
            traversal(root.left, res)
            traversal(root.right, res)
        traversal(root, res)
        sorted_res = sorted(res.items(), key=lambda d:d[1], reverse=True)
        return [d[0] for d in sorted_res if d[1] == sorted_res[0][1]]