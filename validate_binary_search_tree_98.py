/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    min, max := 0, 0
    tmp := root
    for tmp != nil {
        min = tmp.Val
        tmp = tmp.Left
    }
    tmp = root
    for tmp != nil {
        max = tmp.Val
        tmp = tmp.Right
    }
    return isValidBSTWithMinMax(root, min-1, max+1)
}

func isValidBSTWithMinMax(root *TreeNode, min, max int) bool {
    if root == nil {
        return true
    }
    if root.Val <= min || root.Val >= max {
        return false
    }
    return isValidBSTWithMinMax(root.Left, min, root.Val) && isValidBSTWithMinMax(root.Right, root.Val, max)
}
