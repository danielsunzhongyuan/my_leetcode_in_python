# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 1
        queue = [root]
        while queue:
            tmp = []
            for node in queue:
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)
                else:
                    tmp.append(None)
                    tmp.append(None)
            length = len(tmp)
            if length == 0:
                break
            i, j = 0, length - 1
            while i < length:
                if tmp[i]:
                    break
                i += 1
            while j >= i:
                if tmp[j]:
                    break
                j -= 1
            if i == j and not tmp[i]:
                break
            tmp = tmp[i:j+1]
            res = max(res, len(tmp))
            queue = tmp
        return res
