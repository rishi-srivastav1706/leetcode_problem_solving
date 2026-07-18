# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = [root]
        left_to_right = True

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right

        return result
   
        