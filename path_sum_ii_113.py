# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        self.dfs(results, [], root, sum)
        return results
        
    def dfs(self, results, prefix, node, remain):
        if not node.left and not node.right:
            if remain == node.val:
                prefix.append(node.val)
                results.append([x for x in prefix])
        if node.left:
            self.dfs(results, prefix + [node.val], node.left, remain - node.val)
        if node.right:
            self.dfs(results, prefix + [node.val], node.right, remain - node.val)
