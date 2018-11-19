"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        length = len(preorder)
        if length == 0:
            return None
        return self.buildTreeRecursion(preorder, inorder, 0, length - 1, 0, length - 1)

    def buildTreeRecursion(self, preorder, inorder, pl, pr, il, ir):
        if pl > pr:
            return

        mid_node = TreeNode(preorder[pl])
        if pl == pr:
            return mid_node

        m = ir
        while m >= il and inorder[m] != preorder[pl]:
            m -= 1
        mid_node.left = self.buildTreeRecursion(preorder, inorder, pl + 1, m - il + pl, il, m - 1)
        mid_node.right = self.buildTreeRecursion(preorder, inorder, pr - (ir - m - 1), pr, m + 1, ir)
        return mid_node


def main():
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = s.buildTree(preorder, inorder)
    print root.val
    print root.left.val, root.right.val
    print root.right.left.val, root.right.right.val


if __name__ == "__main__":
    main()
