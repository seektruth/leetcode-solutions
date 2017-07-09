# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import operator

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        root.level = 0
        cons = []
        q = [root]
        while q:
            node = q.pop()
            if not node.level < len(cons):
                cons.append([])
            cons[node.level].append(node.val)
            left = node.left
            right = node.right
            if left:
                left.level = node.level + 1
                q.append(left)
            if right:
                right.level = node.level + 1
                q.append(right)
        return [reduce(operator.add, x)/(len(x)+0.0) for x in cons]

