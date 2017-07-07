class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        q = [(root,0)]
        cons = []
        while q:
            node, h = q.pop()
            if node.left: q.insert(0,(node.left, h + 1))
            if node.right: q.insert(0, (node.right, h + 1))
            if not q or q[0][1] > h: cons.append(node.val)
        return cons

    