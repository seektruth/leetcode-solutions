
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        TreeNode.sum = 0
        c = [0]
        def s(node):
            node.sum = 0
            if node.left: node.sum += s(node.left)
            if node.right: node.sum += s(node.right)
            return node.sum
        def r(node):
            left = node.left.sum if node.left else 0
            right = node.right.sum if node.right else 0
            c[0] += abs(left - right)
            if node.left: r(node.left)
            if node.right: r(node.right)
        s(root)
        r(root)
        return c[0]

