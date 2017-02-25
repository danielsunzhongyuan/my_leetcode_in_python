# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        # Solution One
        # if not root:
        #     return []
        # res, stack = [], [(root, "")]
        # while stack:
        #     node, path = stack.pop()
        #     if not node.left and not node.right:
        #         res.append(path + str(node.val))
        #     if node.right:
        #         stack.append((node.right, path + str(node.val) + "->"))
        #     if node.left:
        #         stack.append((node.left, path + str(node.val) + "->"))
        # return res
        
        # Solution Two
        # if not root:
        #     return []
        # res, queue = [], collections.deque([(root, "")])
        # while queue:
        #     node, path = queue.popleft()
        #     if not node.left and not node.right:
        #         res.append(path + str(node.val))
        #     if node.left:
        #         queue.append((node.left, path + str(node.val) + "->"))
        #     if node.right:
        #         queue.append((node.right, path + str(node.val) + "->"))
        # return res
        
        # Solution Three
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res
    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left:
            self.dfs(root.left, path+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, path+str(root.val)+"->", res)
