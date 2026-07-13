class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        
        arr =[]
        queue = []
        queue.append(root)
        while  queue:
            size = len(queue)
            arr1 = []
            for i  in range(size):
                curr = queue.pop(0)
                arr1.append(curr.val) 
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            arr.append(arr1)
        return arr


        