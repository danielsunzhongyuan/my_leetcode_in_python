# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('inf')]
        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            if node.left and node.left.val < res[0]:
                traverse(node.left)
            if node.right and node.right.val < res[0]:
                traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]


def main():
	s = Solution()
	root1 = TreeNode(2)
	root1.left = TreeNode(2)
	root1.right = TreeNode(5)
	root1.right.left = TreeNode(5)
	root1.right.right = TreeNode(7)
	print s.findSecondMinimumValue(root1)

	root2 = TreeNode(1)
	root2.left = TreeNode(1)
	root2.right = TreeNode(2)
	root2.left.left = TreeNode(1)
	root2.left.right = TreeNode(1)
	root2.right.left = TreeNode(2)
	root2.right.right = TreeNode(2)
	print s.findSecondMinimumValue(root2)



if __name__ == "__main__":
	main()
