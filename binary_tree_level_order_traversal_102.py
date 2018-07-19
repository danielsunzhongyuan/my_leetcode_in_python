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
        res = []
        if not root:
            return res
        q1 = collections.deque()
        q2 = collections.deque()
        order = 1
        q1.append(root)
        while q1 or q2:
            res.append([])
            if order == 1:
                while q1:
                    node = q1.popleft()
                    res[-1].append(node.val)
                    if node.left: q2.append(node.left)
                    if node.right: q2.append(node.right)
                order = 0
            else:
                while q2:
                    node = q2.popleft()
                    res[-1].append(node.val)
                    if node.left: q1.append(node.left)
                    if node.right: q1.append(node.right)
                order = 1
        return res

	def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        level = [root]
        while level:
            res.append([node.val for node in level])
            tmp = []
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level = tmp
        return res
